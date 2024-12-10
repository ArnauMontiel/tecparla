import numpy as np
def logPdgm(x):
   return np.log(np.abs(np.fft.fft(x)) + eps)
