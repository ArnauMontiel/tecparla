import numpy as np
from util import *

class Euclidio:
    def __init__(self, *,lisFon=None, ficMod=None):
        if lisFon and ficMod or not (lisFon or ficMod):
            raise('ERROR: lisFon o ficMod deben ser distintos de None.')
        if lisFon:
            self.unidades = leeLis(lisFon)
            self.modelo = {}
        else:
            with open(ficMod, 'rb') as fpMod:
                self.modelo = np.load(fpMod, allow_pickle=True).item()
                self.unidades = self.modelo.keys()

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
            self.modelo[unidad] = self.total[unidad] / self.numUdf[unidad] 
            distancia += (self.total2[unidad] / self.numUdf[unidad] - self.modelo[unidad] **2)
            
        self.distancia = np.sum(distancia) **0.5

    def printEvo(self): 
        print(f'{self.distancia = :.2f}')

    def escMod(self, ficMod):
        chkPathName(ficMod)
        with open(ficMod, 'wb') as fpMod:
            np.save(fpMod, self.modelo)

    def __call__(self, prm):
        minDist = np.inf
        for unidad in self.unidades:
            distancia = np.sum((prm - self.modelo[unidad])**2)
            if distancia < minDist:
                minDist = distancia
                reconocida = unidad

        return reconocida, -minDist




        