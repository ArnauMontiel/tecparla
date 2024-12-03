#!/usr/bin/python3

import numpy as np
from util import *
from ramses.prm import *
from mar import *
from tqdm import tqdm 

def entrena(dirPrm, dirMar, LisFon, ficMod, *figGui):
    
    unidades = leeLis(LisFon)
    total = {unidad : 0 for unidad in unidades}
    numUdf = {unidad : 0 for unidad in unidades}
    modelo = {}
    for senyal in tqdm(leeLis(*figGui), ascii="-/|\|"):
        pathMar = pathName(dirMar, senyal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, senyal, 'prm')
        prm = leePrm(pathPrm)
        total[unidad] += prm
        numUdf[unidad] += 1

    for unidad in unidades:
        modelo[unidad] = total[unidad] / numUdf[unidad]    
    chkPathName(ficMod)
    with open(ficMod, 'wb') as fpMod:
       np.save(fpMod, modelo)

if __name__ == '__main__' :
   # entrena('prm', 'Sen', 'Lis/vocales.lis', 'mod/modelo.mod', 'Gui/train.gui')

   from docopt import docopt
   import sys

   sinopsis = f"""        
    Hace el entrenamiento de reconocimiento.

Usage:
    {sys.argv[0]} [options] <guiSen>...
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version

Opciones: 
    --dirPrm, -p PATH  directorio con los ficheros resultantes del parametriza.
    --dirMar, -m PATH  directorio con las transcripciones de las señales. [default: .]
    --LisFon, -l PATH  Lista de fonemas.
    --ficMod, -f PATH 
    

Diccionario:
    <guiSen> fichero/s guia. 
""" 
   args = docopt(sinopsis, version='tecparla24')
   dirPrm = args['--dirPrm']
   dirMar = args['--dirMar']
   Lisfon = args['--LisFon']
   ficMod = args['--ficMod']
   figGui = args['<guiSen>']

   entrena(dirPrm, dirMar, Lisfon, ficMod, *figGui)



