import numpy as np
from util import *
from scipy.stats import multivariate_normal

class Gaussia:
    def __init__(self, *,lisFon=None, ficMod=None):
        if lisFon and ficMod or not (lisFon or ficMod):
            raise('ERROR: lisFon o ficMod deben ser distintos de None.')
        if lisFon:
            self.unidades = leeLis(lisFon)
            self.media = {}
            self.varianza = {}
            self.gaussiana = {}
        else:
            with open(ficMod, 'rb') as fpMod:
                self.media = np.load(fpMod, allow_pickle=True).item()
                self.varianza = np.load(fpMod, allow_pickle=True).item()
                self.unidades = self.media.keys()
            self.gaussiana = {}
            
            for unidad in self.unidades:
                self.gaussiana[unidad] = multivariate_normal(mean=self.media[unidad], cov=self.varianza[unidad], allow_singular=True)

    def initMod(self):
        self.total = {unidad : 0 for unidad in self.unidades}
        self.total2 = {unidad : 0 for unidad in self.unidades}
        self.numUdf = {unidad : 0 for unidad in self.unidades}

    def addPrm(self, prm, unidad):
        
        self.total[unidad] += prm
        self.total2[unidad] += prm **2
        self.numUdf[unidad] += 1

    def recaMod(self):
        distancia = 0
        for unidad in self.unidades:
            self.media[unidad] = self.total[unidad] / self.numUdf[unidad]
            self.varianza[unidad] = self.total2[unidad] / self.numUdf[unidad] - self.media[unidad]**2 
            distancia += (self.total2[unidad] / self.numUdf[unidad] - self.media[unidad] **2)
            
            self.gaussiana[unidad] = multivariate_normal(mean=self.media[unidad], cov=self.varianza[unidad], allow_singular=True)
            
        self.distancia = np.sum(distancia) **0.5

    def printEvo(self): 
        print(f'{self.distancia = :.2f}')

    def escMod(self, ficMod):
        chkPathName(ficMod)
        with open(ficMod, 'wb') as fpMod:
            np.save(fpMod, self.media)
            np.save(fpMod, self.varianza)

    def __call__(self, prm):
        maxProb = -np.inf
        for unidad in self.unidades:
            probabilidad = self.gaussiana[unidad].logpdf(prm)
            if probabilidad > maxProb:
                maxProb = probabilidad
                reconocida = unidad
       

        return reconocida, maxProb




        