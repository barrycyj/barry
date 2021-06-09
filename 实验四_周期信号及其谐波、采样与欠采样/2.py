import matplotlib.pyplot as plt
from thinkdsp import SquareSignal
from thinkdsp import decorate
from thinkdsp import CosSignal

#方波
signal = SquareSignal(1100)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(2,2,1)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
plt.subplot(2,2,2)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

#混叠
signal = CosSignal(4500)
duration = signal.period*5
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(2,2,3)
segment.plot()
decorate(xlabel='Time (s)')

signal = CosSignal(5500)
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(2,2,4)
segment.plot()

decorate(xlabel='Time (s)')
plt.show()