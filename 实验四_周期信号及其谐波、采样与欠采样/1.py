from thinkdsp import TriangleSignal
from thinkdsp import SquareSignal
from thinkdsp import SawtoothSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

#三角波
signal = TriangleSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,1)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
plt.subplot(3,2,2)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

#方波
signal = SquareSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,3)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
plt.subplot(3,2,4)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

#锯齿波
signal = SawtoothSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,5)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
plt.subplot(3,2,6)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

plt.show()



