import numpy as np
from util import *
from torch.nn.functional import nll_loss
from torch.optim import SGD
import torch

class RedPT:
    def __init__(self, *,lisFon=None, ficMod=None, red=None, funcLoss=nll_loss, 
                 Optim=lambda params: SGD(params, lr=1e-5)):
        if lisFon and ficMod or not (lisFon or ficMod):
            raise('ERROR: lisFon o ficMod deben ser distintos de None.')
        if lisFon:
            self.unidades = leeLis(lisFon)
            self.red = red
            self.red.unidades = self.unidades
            
        else:
            self.leeMod(ficMod)
        self.funcLoss = funcLoss
        self.optim = Optim(self.red.parameters())

    def leeMod(self, ficMod):
        self.red = torch.jit.load(ficMod)

    def escMod(self, ficMod):
        chkPathName(ficMod)
        torch.jit.script(self.red).save(ficMod)
              
    def initMod(self):
        self.optim.zero_grad()
        self.loss = 0
        self.numni = 0
        self.cor = 0.

    def addPrm(self, prm, unidad):
        salida = self.red(prm).swapdims(1,2)
        loss = self.funcLoss(salida, torch.tensor([self.unidades.index(unidad)]))
        loss.backward()
        self.loss += loss
        self.numni += 1
        self.cor += self(prm) == self.unidades.index(unidad)
        return self

    def recaMod(self):
        self.optim.step()
        self.loss /= self.numni
        self.cor /= self.numni

    def printEvo(self): 
        print(f'{self.loss = } {self.cor= }')

    
    def __call__(self, prm):
             
        return self.red.unidades[self.red(prm).argmax()]
    
    

        

    






        