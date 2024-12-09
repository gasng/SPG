import numpy as np


def sta_lta(signal, nsta, nlta, threshold_p, threshold_s):
    squared_signal = signal ** 2
    sta = np.convolve(squared_signal, np.ones(nsta) / nsta, mode='full')[:len(signal)]
    lta = np.convolve(squared_signal, np.ones(nlta) / nlta, mode='full')[:len(signal)]
    sta_lta = sta / lta
    sta_lta[:nlta] = 1

    p_idx = np.where(sta_lta > threshold_p)[0]
    if len(p_idx) > 0:
        p_idx = p_idx[0]
    else:
        p_idx = None

    s_idx = None
    if p_idx is not None:
        s_idx = np.where(sta_lta[p_idx:] > threshold_s)[0]
        if len(s_idx) > 0:
            s_idx = p_idx + s_idx[0]

    return p_idx, s_idx, sta_lta

nsta = 10
nlta = 50