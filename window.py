from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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

        back_btn = QAction(QIcon(resource_path('./assets/left_arrow.png')), "Back" , self)
        back_btn.triggered.connect(self.tabs.currentWidget().back)
        
        forward_btn = QAction(QIcon(resource_path('./assets/right_arrow.png')), "Forward", self)
        forward_btn.triggered.connect(self.tabs.currentWidget().forward)

        reload_btn = QAction(QIcon(resource_path('./assets/reload.png')),'Reload', self)
        reload_btn.triggered.connect(self.tabs.currentWidget().reload)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        add_btn = QAction(QIcon(resource_path('./assets/plus.png')), 'Add', self)
        add_btn.triggered.connect(lambda: self.add_new_tab())
        
        self.navbar.addActions([back_btn, forward_btn, add_btn, reload_btn])
        self.navbar.addWidget(self.url_bar)

        self.tabs.currentWidget().urlChanged.connect(self.update_url)
        self.tabs.currentChanged.connect( self.current_tab_changed )


    def add_new_tab(self, qurl=None, label="Blank"):
    
        if qurl is None:
            qurl = QUrl('https://www.google.com/')

        browser = QWebEngineView()
        browser.setUrl( qurl )
        i = self.tabs.addTab(browser, 'Google')

        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect( lambda qurl, browser=browser:
                self.url_bar.setText(qurl.toString()))

        browser.loadFinished.connect( lambda _, i=i, browser=browser:
            self.tabs.setTabText(i, browser.page().title()) )

    def close_current_tab(self, i):
        self.tabs.removeTab(i)

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.tabs.currentWidget().setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.url_bar.setText(qurl.toString())
