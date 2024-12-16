import numpy as np
import matplotlib.pyplot as plt
from obspy import read

# Загрузка данных
def load_data(filename, id):
    return read(filename)[id*3:(id+1)*3]

# График и события
class SeismicDataPlotter:
    def __init__(self, data, id):
        self.id = id+1
        self.data = data
        self.time = self.data[0].times()
        colors = ['green', 'red', 'blue']
        labels = ['East', 'North', 'Vertical']
        fig, ax = plt.subplots(3, 1, sharex=True, sharey=True, figsize=(10, 8))
        fig.suptitle(f'Показания сейсмического приёмника №{self.id}')
        for self.trace, axi, i in zip(self.data.traces, ax, [0,1,2]):
            axi.plot(self.time, self.trace.data, c=colors[i], label=labels[i])
            axi.set_xlabel('Время (c)')
            axi.set_ylabel('Амплитуда')
            axi.legend()
        self.fig = fig
        self.ax = ax
        self.first_p_wave = None
        self.first_s_wave = None

        # Подписываем обработчик событий
        self.cid_click = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid_key = self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        plt.show()

    def on_click(self, event):
        # Проверяем, что на графике происходит клик
        if event.button == 3:  # Правая кнопка мыши
            time_clicked = event.xdata
            if self.first_p_wave is None: # Первое нажатие
                self.first_p_wave = time_clicked
                for axi in self.ax:
                    axi.axvline(x=self.first_p_wave, color='purple', linestyle='--', label='P-волнa')
                    axi.legend()
                self.fig.canvas.draw()
            elif self.first_s_wave is None: # Второе нажатие
                self.first_s_wave = time_clicked
                for axi in self.ax:
                    axi.axvline(x=self.first_s_wave, color='gray', linestyle='--', label='S-волнa')
                    axi.legend()
                self.fig.canvas.draw()

    def on_key(self, event):
        # Удаление неверно снятого вступления
        if event.key == 'delete':
            # Стираем линии
            if self.first_s_wave is not None:
                for axi in self.ax:
                    for line in axi.lines:
                        if line.get_xdata()[0] == self.first_s_wave:
                            line.remove()
                self.first_s_wave = None
            elif self.first_p_wave is not None:
                for axi in self.ax:
                    for line in axi.lines:
                        if line.get_xdata()[0] == self.first_p_wave:
                            line.remove()
                self.first_p_wave = None
            self.fig.canvas.draw()
        # Снять выбранные значения
        elif event.key == 'enter':
            # Выводим времена вступления волн
            if self.first_p_wave is not None and self.first_s_wave is not None:
                print(f'Приемник №{self.id}')
                print(f'Первое вступление P-волн: {self.first_p_wave:.2f} с')
                print(f'Первое вступление S-волн: {self.first_s_wave:.2f} с')
            else:
                print('Убедитесь, что обе волны выбраны.')

# Файл с данными
filename = 'C:/Users/Danil/Downloads/test.mseed'
for i in range (len(read(filename)) // 3):
    data = load_data(filename, i)
    SeismicDataPlotter(data, i)
