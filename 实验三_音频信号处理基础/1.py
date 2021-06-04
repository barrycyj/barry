from thinkdsp import CosSignal, SinSignal,Wave
import copy
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import scipy
import scipy.stats
import scipy.fftpack
import subprocess
import warnings

from wave import open as open_wave
from scipy.io import wavfile
from thinkdsp import decorate
from IPython.display import Audio

from thinkdsp import read_wave
wave = read_wave('92002__jcveliz__violin-origional.wav')
wave.make_audio()

def stretch(sign,ts,framerate):
    sign.ts+=ts
    sign.framerate*=framerate
    return sign


wave = read_wave('92002__jcveliz__violin-origional.wav')
segment = wave.segment()
spectrum = segment.make_spectrum()
plt.subplot(2,1,1)
spectrum.plot()

decorate(xlabel='Frequency (Hz)')


wave=stretch(wave,1,2)
segment = wave.segment()
spectrum = segment.make_spectrum()
plt.subplot(2,1,2)
spectrum.plot()

decorate(xlabel='Frequency (Hz)')
plt.show()
