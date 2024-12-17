from python_speech_features import mfcc as mfcc_
def mfcc(x):
   return mfcc_(x, samplerate=8000, winlen=0.064, winstep=0.064, numcep=32,nfilt=48) [0]
