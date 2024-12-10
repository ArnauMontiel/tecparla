import numpy as np
def BlackmanTukey(x):
   N = len(x)
   orden = 32
   cor = np.correlate(x, x, mode='full')
   wcor = cor[N-orden-1:N+orden] * np.bartlett(2 * orden + 1)
   return np.log(np.abs(np.fft.fft(wcor, n = N))**2 + 10)
