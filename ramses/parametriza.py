#!/usr/bin/python3

from util import *
import soundfile as sf
#import prm #
from prm import *
from tqdm import tqdm #progress bar

def parametriza(dirPrm, dirSen, *guiSen, funcPrm=np.array):
    ficheros = leeLis(*guiSen)
    for fichero in tqdm((ficheros), ascii="-/|\|"):
        pathSen = pathName(dirSen, fichero,'wav')
        sen, fm = sf.read(pathSen)
        prm = funcPrm(sen)
        pathPrm = pathName(dirPrm, fichero, 'prm')
        chkPathName(pathPrm)
        escrPrm(pathPrm, prm)


if __name__ == '__main__' : 
    #parametriza('prm', 'Sen', "Gui/train.gui", 'Gui/devel.gui', 'Gui/eval.gui')

   from docopt import docopt
   import sys

   sinopsis = f"""        
    Parametriza la señal.

Usage:
    {sys.argv[0]} [options] <guiSen>...
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version

Opciones: 
    --dirPrm, -p PATH  directorio con las señales parametrizadas..
    --dirSen, -s PATH  directorio con las señales de entrada.
    --execPre, -x SCRIPTS  scripts a ejecutar antes de la parametrizacion.
    --funcPrm, -f EXPR  expresion que proporciona la función de parametrizacion [default: np.array]
    
Diccionario:
    <guiSen> fichero/s guia. 
""" 
   args = docopt(sinopsis, version='tecparla24')
   dirPrm = args['--dirPrm']
   dirSen = args['--dirSen']
   guiSen = args['<guiSen>']

   scripts = args['--execPre']
   if scripts:
       for script in scripts.split(','):
           exec(open(script).read()) 


   funcPrm = eval(args['--funcPrm'])

   parametriza(dirPrm, dirSen, *guiSen, funcPrm=funcPrm)


   


     

    
