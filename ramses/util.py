
from pathlib import Path
def leeLis(*ficLis):
    lista = []

    for fichero in ficLis:
        with open(fichero, 'rt') as fplis: 
            lista += [palabra.strip() for palabra in fplis]


    return lista

def pathName(dir, nom, ext):

    return dir + '/' + nom + '.' + ext 

def chkPathName(path):

    Path(path).parent.mkdir(parents=True, exist_ok=True)

