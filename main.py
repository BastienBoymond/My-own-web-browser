import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import MainWindow
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


app = QApplication(sys.argv)
QApplication.setApplicationName("Own Browser")
QApplication.setWindowIcon(QIcon(resource_path('./assets/kaguya.png')))
window = MainWindow()
app.exec_();


