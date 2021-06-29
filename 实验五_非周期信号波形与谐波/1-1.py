from thinkdsp import decorate
from thinkdsp import Chirp
import matplotlib.pyplot as plt
import numpy as np

signal=Chirp(start=220,end=880)
wave1=signal.make_wave()
wave1.make_audio()


wave1.segment(start=0.9, duration=0.01).plot()

decorate(xlabel='Time (s)')

plt.show()