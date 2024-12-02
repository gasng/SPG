class Preproc:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    # Детренд - просто вставка из scipy.signal. Если необходимо расписать его более эффективно - можно перепрописать.
    # Пока что нужен для простой проверки работа гитхаба. Пока даже закоментирую сам код.
    def detrend(self):
        return self.data # scipy.signal.detrend(self.data)