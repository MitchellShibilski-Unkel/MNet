import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *


class MNet(QMainWindow):
    def __init__(self, caption: str, width: int, height: int, backBtnIcon: str = "←", forwardBtnIcon: str = "→", reloadBtnIcon: str = "⟳"):
        super(MNet, self).__init__()
        self.browser = QWebEngineView()
        
        # Set the title of the window
        self.setWindowTitle(caption)
        
        # Set default window size
        self.resize(width, height)
        
        # --- Create the UI --- #
        # Search engine
        self.showMaximized()
        self.setCentralWidget(self.browser)
        
        # Nav
        self.navbar = QToolBar()
        self.navbar.setFont(QFont("Arial", 10))
        self.navbar.setStyle(QStyleFactory.create("Fusion"))
        self.addToolBar(self.navbar)
        self.__addButton__(backBtnIcon, "b"), self.__addButton__(forwardBtnIcon, "f"), self.__addButton__(reloadBtnIcon, "r"), self.__addButton__("\U0001F4CB", "c")
        
        self.urlText = QLineEdit()
        self.urlText.returnPressed.connect(self.openURL)
        self.navbar.addWidget(self.urlText)
        self.browser.urlChanged.connect(self.updateURL)
        
        self.__find__()

    def openURL(self):
        url = self.urlText.text()
        self.browser.setUrl(QUrl(url))

    def updateURL(self, q):
        self.urlText.setText(q.toString())
        
    def navBarCanMove(self, can: bool):
        self.navbar.setMovable(can)
        
    def setDefaultUI(self, fontColor: str, navBackgroundColor: str, searchEngineColor = "white", textAlign = "left"):
        self.navbar.setStyleSheet(f"background-color: {navBackgroundColor}; color: {fontColor};")
        if searchEngineColor in "white":
            if textAlign in "center":
                self.browser.setUrl(QUrl("https://duckduckgo.com/?kae=-1&ks=t&kau=-1&kak=-1&kax=-1&km=m"))
            else:
                self.browser.setUrl(QUrl("https://duckduckgo.com/?kae=-1&ks=t&kau=-1&kak=-1&kax=-1&km"))
        elif searchEngineColor in "black":
            if textAlign in "center":
                self.browser.setUrl(QUrl("https://duckduckgo.com/?kae=d&ks=t&kau=-1&kak=-1&kax=-1&km=m"))
            else:
                self.browser.setUrl(QUrl("https://duckduckgo.com/?kae=d&ks=t&kau=-1&kak=-1&kax=-1&km"))
        else:
            print("ERROR :: Invalid search engine color; needs to be 'white' or 'black'")
        
    def __find__(self):
        findBar = QLineEdit()
        findBar.setPlaceholderText("Find...")
        self.navbar.addWidget(findBar)
        
        print(findBar.text())
        
        if findBar.text() == "Find..." or findBar.text() == "": 
            find = self.browser.findText(findBar.text())
            print(find)
        
    def __addButton__(self, icon: str, action: str):
        btn = QAction(icon, self)
        if action in "f":
            btn.triggered.connect(self.browser.forward)
        if action in "b":
            btn.triggered.connect(self.browser.back)
        if action in "r":
            btn.triggered.connect(self.browser.reload)
        if action in "c":
            btn.triggered.connect(lambda: QGuiApplication.clipboard().setText(self.browser.url().toString()))
            
        self.navbar.addAction(btn)
        
app = QApplication(sys.argv)
window = MNet("MNet", 500, 500)
window.navBarCanMove(False)
window.setDefaultUI("gray", "black")
app.exec()
