import numpy as np

def escrPrm(pathPrm, prm):
    
    with open(pathPrm,'wb') as fp_rpm:
        np.save(fp_rpm, prm)

def leePrm(pathPrm):
    with open(pathPrm,'rb') as fp_rpm:
        prm = np.load(fp_rpm)
        return prm



