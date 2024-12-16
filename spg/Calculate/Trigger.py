import numpy as np
import matplotlib.pyplot as plt
import obspy


def sta_lta(signal, nsta, nlta, threshold_ON, threshold_OFF):
    squared_signal = signal ** 2
    sta = np.convolve(squared_signal, np.ones(nsta) / nsta, mode='full')[:len(signal)]
    lta = np.convolve(squared_signal, np.ones(nlta) / nlta, mode='full')[:len(signal)]
    sta_lta = sta / lta
    sta_lta[:nlta] = 0

    ON_idx = np.where(sta_lta > threshold_ON)[0]
    if len(ON_idx) > 0:
        ON_idx = ON_idx[0]
    else:
        ON_idx = None

    OFF_idx = None
    if ON_idx is not None:
        OFF_idx = np.where(sta_lta[ON_idx:] < threshold_OFF)[0]
        if len(OFF_idx) > 0:
            OFF_idx = ON_idx + OFF_idx[0]

    return ON_idx, OFF_idx, sta_lta


def MER(signal, n, threshold_ON, threshold_OFF):
    squared_signal = signal ** 2
    right = np.array([np.sum(squared_signal[i: i + n]) for i in range(n - 1, len(squared_signal) - n + 1)])
    left = np.array([np.sum(squared_signal[i: i + n]) for i in range(0, len(squared_signal) - 2 * n + 2)])
    MER = [1 for i in range(n)]
    ER = right / left
    M = np.abs(signal[n - 1:len(signal) - n + 1:])
    MER = MER + list((ER * M) ** 3)
    MER = np.array(MER)

    ON_idx = np.where(MER > threshold_ON)[0]
    if len(ON_idx) > 0:
        ON_idx = ON_idx[0]
    else:
        ON_idx = None

    OFF_idx = None
    if ON_idx is not None:
        OFF_idx = np.where(MER[ON_idx:] < threshold_OFF)[0]
        if len(OFF_idx) > 0:
            OFF_idx = ON_idx + OFF_idx[0]

    return ON_idx, OFF_idx, MER