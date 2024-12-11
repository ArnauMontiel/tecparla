import numpy as np
from util import *

class Euclidio:
    def __init__(self, LisFon):
        self.unidades = leeLis(LisFon)
        self.modelo = {}

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




        