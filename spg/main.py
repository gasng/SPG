import os.path

from PySide6.QtWidgets import QWidget, QApplication, QFileDialog
import sys

from spg.UI import Ui_ReadWidget

#Коментарий на возможность

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_ReadWidget()
        self.ui.setupUi(self)
        self.__create_callbacks()

    def __create_callbacks(self):
        self.ui.ChooseBtn.clicked.connect(self.__get_filenames)
        self.ui.ReadLW.clicked.connect(self.__print_filename)

    def __get_filenames(self):
        self.ui.ReadLW.clear()
        filepaths, _ = QFileDialog.getOpenFileNames(self, "Выбери нужные файлы",
                        "",
                        "Scripts (*.py)"
                                                )
        filenames = [os.path.basename(filepath) for filepath in filepaths]
        self.ui.ReadLW.addItems(filenames)

    def __print_filename(self):
        item = self.ui.ReadLW.currentItem().text()
        print(item)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    return app.exec_()


if getattr(sys, 'frozen', False):
    main()
