from scipy import signal

def lin_detrend(data):
    return signal.detrend(data, type='linear')

def const_detrend(data):
    return signal.detrend(data, type='constant')

def deconvolution(data):
    return data

def butter_lowpass(lowcut, fs, order=5):
    return signal.butter(order, lowcut, fs=fs, btype='low')
def butter_lowpass_filter(data, lowcut, fs, order=5):
    b, a = butter_lowpass(lowcut, fs, order=order)
    filtered_data = signal.lfilter(b, a, data)
    return filtered_data


def butter_highpass(highcut, fs, order=5):
    return signal.butter(order, highcut, fs=fs, btype='high')
def butter_highpass_filter(data, highcut, fs, order=5):
    b, a = butter_highpass(highcut, fs, order=order)
    filtered_data = signal.lfilter(b, a, data)
    return filtered_data


def butter_bandpass(lowcut, highcut, fs, order=5):
    return signal.butter(order, [lowcut, highcut], fs=fs, btype='band')
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    filtered_data = signal.lfilter(b, a, data)
    return filtered_data
