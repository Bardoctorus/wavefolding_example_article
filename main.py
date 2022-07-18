import numpy as np
import matplotlib.pyplot as plt
import audio_dspy as adsp

fs = 44100

def tri_wave(x, freq, fs):
    p = float((1/freq) * fs)
    x = x + p/4
    return 4 * np.abs((x / p) - np.floor((x / p) + 0.5)) -1

def sine_wave(x, freq, fs):
    return np.sin(2 * np.pi * x * freq/fs)


plt.figure()
adsp.plot_static_curve(lambda x : tri_wave(x, fs/2, fs),gain = 5)
plt.title('Triangle wavefolder Static Curve')

plt.figure()
adsp.plot_static_curve(lambda x : sine_wave(x, fs/2, fs), gain = 5)
plt.title('Sine Wavefolder Static Curve')

plt.show()

