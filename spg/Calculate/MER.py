import numpy as np

def MER(signal, n, threshold_p, threshold_s):
    squared_signal = signal ** 2
    right = np.array([np.sum(squared_signal[i: i + n]) for i in range(n - 1, len(squared_signal) - n + 1)])
    left = np.array([np.sum(squared_signal[i: i + n]) for i in range(0, len(squared_signal) - 2 * n + 2)])
    ER = right / left
    M = np.array([abs(i) for i in signal[n - 1:len(signal) - n + 1:]])
    MER = (ER * M)

    p_idx = np.where(MER > threshold_p)[0]
    if len(p_idx) > 0:
        p_idx = p_idx[0]
    else:
        p_idx = None

    s_idx = None
    if p_idx is not None:
        s_idx = np.where(MER[p_idx:] > threshold_s)[0]
        if len(s_idx) > 0:
            s_idx = p_idx + s_idx[0]

    return p_idx, s_idx, MER