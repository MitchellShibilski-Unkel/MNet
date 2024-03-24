import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MNet(QMainWindow):
    def __init__(self, url: str, caption: str):
        super(MNet, self).__init__()
        self.browser = QWebEngineView()
        
        # Set the title of the window
        self.setWindowTitle(caption)
        
        # Set default search engine
        self.browser.setUrl(QUrl(url))
        
        # --- Create the UI --- #
        # Search engine
        self.showMaximized()
        self.setCentralWidget(self.browser)
        
        # Nav
        self.navbar = QToolBar()
        self.addToolBar(self.navbar)
        self.__addButton__("←", "b"), self.__addButton__("→", "f"), self.__addButton__("⟳", "r")
        
        self.urlText = QLineEdit()
        self.urlText.returnPressed.connect(self.openURL)
        self.navbar.addWidget(self.urlText)
        self.browser.urlChanged.connect(self.updateURL)

    def openURL(self):
        url = self.urlText.text()
        self.browser.setUrl(QUrl(url))

    def updateURL(self, q):
        self.urlText.setText(q.toString())
        
    def __addButton__(self, icon: str, action: str):
        btn = QAction(icon, self)
        if action in "f":
            btn.triggered.connect(self.browser.forward)
        if action in "b":
            btn.triggered.connect(self.browser.back)
        if action in "r":
            btn.triggered.connect(self.browser.reload)
            
        self.navbar.addAction(btn)
        
app = QApplication(sys.argv)
window = MNet('https://duckduckgo.com/?kae=-1&ks=t&kau=-1&kak=-1&kax=-1&km=m', "MNet")
app.exec()