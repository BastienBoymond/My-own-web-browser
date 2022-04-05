import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import MainWindow

app = QApplication(sys.argv)
QApplication.setApplicationName("Own Browser")
QApplication.setWindowIcon(QIcon('./assets/kaguya.png'))
window = MainWindow()
app.exec_();


