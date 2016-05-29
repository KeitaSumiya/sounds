import wave
import numpy as np
import struct


def makewave(amp,freq,sec,fs=44100):
    outwave = []
    for i in range(sec*fs):
        w = amp*np.sin(2*np.pi*freq*i/fs)
        outwave.append(w)
    return(outwave)


def wavwrite(inputlist,filename):
    maxamp = 32767.0
    int16wave = [int(x * maxamp) for x in inputlist]
    binwave = struct.pack("h"*len(int16wave),*int16wave)

    nchannnles = 1 # 1=monoral , 2=stereo
    sampwitdth = 2 # 1=8bit,2=16bit,3=,...
    framerate = 44100 # sampling rate ex.44100Hz
    nframes = len(inputlist) # framerate * sec
    
    of = wave.open(filename,"w")
    of.setparams((nchannnles,sampwitdth,framerate,nframes,"NONE","not compressed"))
    of.writeframes(binwave)
    of.close



