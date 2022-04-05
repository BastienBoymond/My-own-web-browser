from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.showMaximized()
        
        #NavBar
        self.navbar = QToolBar()
        self.addToolBar(self.navbar)

        # Close event
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)        

        #Create First Tab
        self.add_new_tab();

        back_btn = QAction(QIcon('./assets/left_arrow.png'), "Back" , self)
        back_btn.triggered.connect(self.tabs.currentWidget().back)
        
        forward_btn = QAction(QIcon('./assets/right_arrow.png'), "Forward", self)
        forward_btn.triggered.connect(self.tabs.currentWidget().forward)

        reload_btn = QAction(QIcon('./assets/reload.png'),'Reload', self)
        reload_btn.triggered.connect(self.tabs.currentWidget().reload)

        add_btn = QAction(QIcon('./assets/plus.png'), 'Add', self)
        add_btn.triggered.connect(lambda: self.add_new_tab())
        self.navbar.addActions([back_btn, forward_btn, reload_btn, add_btn])


    def add_new_tab(self, qurl=None, label="Blank"):
    
        if qurl is None:
            qurl = QUrl('https://www.google.com/')

        browser = QWebEngineView()
        browser.setUrl( qurl )
        i = self.tabs.addTab(browser, 'Google')

        self.tabs.setCurrentIndex(i)



    def close_current_tab(self, i):
        self.tabs.removeTab(i)

