#!/usr/bin/python3

import numpy as np
from util import *
from ramses.prm import *
from mar import *
from tqdm import tqdm 


def entrena(dirPrm, dirMar, LisFon, ficMod, *figGui):
    # Construimos el modelo inicial.
    modelo = {}
    unidades = leeLis(LisFon)

    # Inicializamos las estructuras iniciales para el entrenamiento.
    total = {unidad : 0 for unidad in unidades}
    total2 = {unidad : 0 for unidad in unidades}
    numUdf = {unidad : 0 for unidad in unidades}
    
    # Bucle para todas las senyales
    for senyal in tqdm(leeLis(*figGui), ascii="-/|\|"):
        pathMar = pathName(dirMar, senyal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, senyal, 'prm')
        prm = leePrm(pathPrm)

        # INCORPORAMOS la información de la señal al modelo.
        total[unidad] += prm
        total2[unidad] += prm **2
        numUdf[unidad] += 1

    # RECALCULAMOS el modelo.
    distancia = 0
    variancia = 0
    media = 0

    for unidad in unidades:
        modelo[unidad] = total[unidad] / numUdf[unidad] 
        distancia += (total2[unidad] / numUdf[unidad] - modelo[unidad] **2)
        #media += total[unidad] / numUdf[unidad]
    distancia = np.sum(distancia) **0.5
    
    #MOSTRAMOS la evolución del entrenamiento.
    print(f'{distancia = :.2f}')
    
    # ESCRIBIMOS el modelo generado.   
    chkPathName(ficMod)
    with open(ficMod, 'wb') as fpMod:
       np.save(fpMod, modelo)

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



