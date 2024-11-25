import numpy as np

def sta_lta(signal, nsta, nlta):
    squared_signal = signal ** 2
    sta = np.convolve(squared_signal, np.ones(nsta) / nsta, mode='full')[:len(signal)]
    lta = np.convolve(squared_signal, np.ones(nlta) / nlta, mode='full')[:len(signal)]
    sta_lta_ratio = sta / lta
    return sta_lta_ratio

nsta = 5
nlta = 100