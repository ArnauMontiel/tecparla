#!/usr/bin/python3

import numpy as np
from ramses.util import *
from ramses.prm import *
from tqdm import tqdm 
from gaussiano import Gaussia

def reconoce(dirRec, dirPrm, ficMod, Modelo, *guiSen):
    
    modelos = Modelo(ficMod=ficMod)

    for sen in tqdm(leeLis(*guiSen)):
        pathPrm = pathName(dirPrm, sen, 'prm')
        prm = leePrm(pathPrm)
        reconocida, minDist = modelos(prm)
        pathRec = pathName(dirRec, sen, 'rec')
        chkPathName(pathRec)
        with open (pathRec, 'wt') as fpRec:
            fpRec.write(f'LBO: ,,,{reconocida}\n')


if __name__ == '__main__': 
   
   from docopt import docopt
   import sys

   sinopsis = f"""        
Evalua el resultado de un reconocimiento.

Usage:
    {sys.argv[0]} [options] <guiSen>...
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version

Opciones: 
    --dirRec, -r PATH  directorio con los ficheros resultantes del reconocimiento
    --dirPrm, -p PATH  directorio con las transcripciones de las señales. [default: .]
    --ficMod, -m FILE  fichero con el modelo.
    --execPre, -x SCRIPTS Script d'execucio previa, es pot indicar més d'un.
    --clsMod, -c CLASE Clase del modelo

Diccionario:
    <guiSen> fichero/s guia. 
""" 
   args = docopt(sinopsis, version='tecparla24')
   dirRec = args['--dirRec']
   dirPrm = args['--dirPrm']
   ficMod = args['--ficMod']
   guiSen = args['<guiSen>']
   execPre = args['--execPre']
   if execPre:
       for script in execPre.split(','):
           exec(open(script).read())
   clsMod = eval(args['--clsMod'])

   reconoce(dirRec, dirPrm, ficMod, clsMod, *guiSen)


   


