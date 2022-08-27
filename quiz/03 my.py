from PyQt5.QtWidgets import *
import sys

class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.group_box1 = QGroupBox('메뉴')
        self.group_box2 = QGroupBox('투표 목록')
        self.group_box3 = QGroupBox('투표')
        self.group_box4 = QGroupBox('투표 결과')

        self.list = QListWidget()

        self.list.addItem('0')

        self.button1 = QPushButton('메뉴 조회')
        self.button2 = QPushButton('A1')
        self.button2.clicked.connect(self.button_click1)
        self.button3 = QPushButton('A2')
        self.button3.clicked.connect(self.button_click2)
        self.button4 = QPushButton('A3')
        self.button4.clicked.connect(self.button_click3)

        self.progressbar1 = QProgressBar()
        self.progressbar1.setRange(0, 100)
        self.progressbar2 = QProgressBar()
        self.progressbar2.setRange(0, 100)
        self.progressbar3 = QProgressBar()
        self.progressbar3.setRange(0, 100)

        self.value1 = 0
        self.value2 = 0
        self.value3 = 0

        self.progressbar1.setValue(self.value1)
        self.progressbar2.setValue(self.value2)
        self.progressbar3.setValue(self.value3)

        self.text_label = QLabel()
        self.text_label.setText('Q1')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)

        self.vbox_layout3 = QVBoxLayout()
        self.vbox_layout3.addWidget(self.list)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.text_label)
        self.vbox_layout.addWidget(self.button2)
        self.vbox_layout.addWidget(self.button3)
        self.vbox_layout.addWidget(self.button4)

        self.vbox_layout2 = QGridLayout()
        self.vbox_layout2.addWidget(self.progressbar1, 0, 0, 1, 1)
        self.vbox_layout2.addWidget(self.progressbar2, 1, 0, 1, 1)
        self.vbox_layout2.addWidget(self.progressbar3, 2, 0, 1, 1)

        self.group_box1.setLayout(self.hbox_layout)
        self.group_box3.setLayout(self.vbox_layout)
        self.group_box4.setLayout(self.vbox_layout2)
        self.group_box2.setLayout(self.vbox_layout3)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.group_box1, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.group_box2, 1, 0, 4, 1)
        self.grid_layout.addWidget(self.group_box3, 1, 1, 4, 1)
        self.grid_layout.addWidget(self.group_box4, 6, 0, 2, 2)

        self.setLayout(self.grid_layout)

    def button_click1(self):
        self.value1 += 1
        self.progressbar1.setValue(self.value1)

    def button_click2(self):
        self.value2 += 1
        self.progressbar2.setValue(self.value2)

    def button_click3(self):
        self.value3 += 1
        self.progressbar3.setValue(self.value3)

class Tab2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.form_layout = QFormLayout()

        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()
        self.line_edit4 = QLineEdit()

        self.button1 = QPushButton('게시')
        self.button2 = QPushButton('초기화')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)

        self.form_layout.addRow('질문: ', self.line_edit1)
        self.form_layout.addRow('선택지: ', self.line_edit2)
        self.form_layout.addRow('', self.line_edit3)
        self.form_layout.addRow('', self.line_edit4)
        self.form_layout.addRow('', self.hbox_layout)

        self.setLayout(self.form_layout)

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('중앙 블록체인 투표 시스템')

        self.tab1 = Tab1()
        self.tab2 = Tab2()

        self.tab = QTabWidget()
        self.tab.addTab(self.tab1, '투표')
        self.tab.addTab(self.tab2, '투표 생성')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.tab)

        self.setLayout(self.vbox_layout)




def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
