import numpy as np
def ceps(x):
   eps = 10
   numCoef = 32
   ceps = np.fft.ifft(np.log(np.abs(np.fft.fft(x)) + eps))
   return np.real(ceps[1:numCoef + 1])
