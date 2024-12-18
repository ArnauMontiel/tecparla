#!/usr/bin/python3

import numpy as np
from util import *
from ramses.prm import *
from mar import *
from tqdm import tqdm 
from gaussiano import Gaussia


def entrena(dirPrm, dirMar, lisFon, ficMod, Modelo, *figGui):
    # Construimos el modelo inicial.
    modelo = Modelo(lisFon=lisFon)
    
    # Inicializamos las estructuras iniciales para el entrenamiento.
    modelo.initMod()
    
    # Bucle para todas las senyales
    for senyal in tqdm(leeLis(*figGui), ascii="-/|\|"):
        pathMar = pathName(dirMar, senyal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, senyal, 'prm')
        prm = leePrm(pathPrm)

        # INCORPORAMOS la información de la señal al modelo.
        modelo.addPrm(prm, unidad)

    # RECALCULAMOS el modelo.
    modelo.recaMod()
    
    #MOSTRAMOS la evolución del entrenamiento.
    modelo.printEvo()
    
    # ESCRIBIMOS el modelo generado.   
    modelo.escMod(ficMod)

if __name__ == '__main__' :
   

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
    --execPre, -x SCRIPTS Script d'execucio previa es pot indicar més d'un
    --clsMod, -c CLASE Clase del modelo
    

Diccionario:
    <guiSen> fichero/s guia. 
""" 
   args = docopt(sinopsis, version='tecparla24')
   dirPrm = args['--dirPrm']
   dirMar = args['--dirMar']
   Lisfon = args['--LisFon']
   ficMod = args['--ficMod']
   figGui = args['<guiSen>']
   execPre = args['--execPre']
   if execPre:
       for script in execPre.split(','):
           exec(open(script).read())
   clsMod = eval(args['--clsMod'])

   entrena(dirPrm, dirMar, Lisfon, ficMod, clsMod, *figGui)



