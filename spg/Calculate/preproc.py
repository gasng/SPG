import numpy as np
from scipy.signal import butter, lfilter, detrend


def lin_detrend(data):
    return detrend(data, type='linear')


def const_detrend(data):
    return detrend(data, type='constant')


def ipgg_geoph_CFR(f, f0, d):
    CFR = (-f ** 2 * (f0 ** 2 - f ** 2) / ((f0 ** 2 - f ** 2) ** 2 + (2 * d * f0 * f) ** 2) +
           ((2 * d * f0 * f ** 3) / ((f0 ** 2 - f ** 2) ** 2 + (2 * d * f0 * f) ** 2)) * 1j)
    return CFR
def decon_freq_phase(trace, fs, decon_freq, Flp, f0, d, HP):
    # LOW-FREQUENCY DECONVOLUTION
    trace = butter_highpass_filter(data=trace, fs=fs, highcut=decon_freq / 2, order=4)

    if trace.ndim != 1:
        trace = trace.flatten()
        tmp2 = 1
    else:
        tmp2 = 0

    L = len(trace)

    f = Fs / 2 * np.linspace(0, 1, L // 2 + 1)
    f = np.concatenate((-f[::-1][1:], f))

    V = ipgg_geoph_CFR(f[:L], f0, d)
    V[V == 0] = 1
    V = V ** -1

    F = ipgg_geoph_CFR(f[:L], decon_freq, d)

    D = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(trace)))

    if HP == 0:
        R = D * V * F
    elif HP == 1:
        R = D * V * F * ipgg_geoph_CFR(f[:L], decon_freq / 2, d)
    else:
        R = D * V * F * ipgg_geoph_CFR(f[:L], decon_freq, d)

    decon_trace = np.real(np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(R))))
    return decon_trace


def butter_lowpass(lowcut, fs, order=5):
    assert 0 < lowcut < fs / 2, "Digital filter critical frequencies must "f"be 0 < Wn < fs/2 (fs={fs} -> fs/2={fs / 2})"
    return butter(order, lowcut, fs=fs, btype='low')
def butter_lowpass_filter(data, lowcut, fs, order=5):
    b, a = butter_lowpass(lowcut, fs, order=order)
    filtered_data = lfilter(b, a, data)
    return filtered_data


def butter_highpass(highcut, fs, order=5):
    assert 0 < highcut < fs / 2, "Digital filter critical frequencies must "f"be 0 < Wn < fs/2 (fs={fs} -> fs/2={fs / 2})"
    return butter(order, highcut, fs=fs, btype='high')
def butter_highpass_filter(data, highcut, fs, order=5):
    b, a = butter_highpass(highcut, fs, order=order)
    filtered_data = lfilter(b, a, data)
    return filtered_data


def butter_bandpass(lowcut, highcut, fs, order=5):
    assert 0 < lowcut < highcut, "Digital filter lower critical frequencies must "f"be 0 < Wn < highcut (highcut={highcut} -> lowcut+1={lowcut + 1})"
    assert 0 < lowcut and highcut < fs / 2, "Digital filter critical frequencies must "f"be 0 < Wn < fs/2 (fs={fs} -> fs/2={fs / 2})"
    return butter(order, [lowcut, highcut], fs=fs, btype='band')
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    filtered_data = lfilter(b, a, data)
    return filtered_data
