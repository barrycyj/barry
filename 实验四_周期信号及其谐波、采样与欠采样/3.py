from thinkdsp import Spectrum, TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

signal = TriangleSignal(440)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,1,1)
segment.plot()


signal = TriangleSignal(440)
signal.plot()

wave = signal.make_wave(duration=0.01, framerate=10000)

Spectrum=wave.make_spectrum()
plt.subplot(3,1,2)
Spectrum.plot()
decorate(title=Spectrum.hs[0])



Spectrum.hs[0]=100
plt.subplot(3,1,3)
Spectrum.plot()
decorate(title=Spectrum.hs[0])

plt.show()

