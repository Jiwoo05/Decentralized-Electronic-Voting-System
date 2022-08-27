from PyQt5.QtWidgets import *
import sys

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1 = QPushButton('버튼 1')
        self.button2 = QPushButton('버튼 2')
        self.button3 = QPushButton('버튼 3')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)
        self.button3.clicked.connect(self.button3_click)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.button1, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.button2, 1, 0, 1, 2)
        self.grid_layout.addWidget(self.button3, 1, 2, 1, 2)

        self.setLayout(self.grid_layout)

    def button1_click(self):
        self.button1.sefEnabled(False)
        self.button1.setText('버튼 1 클릭')

    def button2_click(self):
        self.button2.sefEnabled(False)
        self.button2.setText('버튼 2 클릭')

    def button3_click(self):
        self.button1.sefEnabled(True)
        self.button2.sefEnabled(True)
        self.button3.sefEnabled(False)
        self.button3.setText('버튼 3 클릭')


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())

