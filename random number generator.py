from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Aplikasi pertama')
my_win.move(900, 70)
my_win.resize(600, 300)
my_win.show()

line = QHBoxLayout()
button = QPushButton('Secret button')
line.addWidget(button , alignment=Qt.AlignCenter)
my_win.setLayout(line)

def show_fun_title():
    fun_title = QLabel('Goodjob')
    line.addWidget(fun_title , alignment=Qt.AlignCenter)
    my_win.setLayout(line)

button.clicked.connect(show_fun_title)
app.exec_()