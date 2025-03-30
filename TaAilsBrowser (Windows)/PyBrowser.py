import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TaAils Browser")
        self.setWindowIcon(QIcon("assets/TaAilsBrowserLogo.png"))
        self.setGeometry(200, 200, 1280, 720)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backBtn = QPushButton()
        self.backBtn.setIcon(QIcon("assets/back.svg"))
        self.backBtn.clicked.connect(self.backButton)
        self.backBtn.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.backBtn)

        self.reloadBtn = QPushButton()
        self.reloadBtn.setIcon(QIcon("assets/reload.svg"))
        self.reloadBtn.clicked.connect(self.reloadButton)
        self.reloadBtn.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.reloadBtn)

        self.forwardBtn = QPushButton()
        self.forwardBtn.setIcon(QIcon("assets/forward.svg"))
        self.forwardBtn.setIconSize(QSize(36, 36))
        self.forwardBtn.clicked.connect(self.forwardButton)
        toolbar.addWidget(self.forwardBtn)

        self.homeBtn = QPushButton()
        self.homeBtn.setIcon(QIcon("assets/home.svg"))
        self.homeBtn.setIconSize(QSize(36, 36))
        self.homeBtn.clicked.connect(self.homeButton)
        toolbar.addWidget(self.homeBtn)

        self.adressBar = QLineEdit()
        self.adressBar.setFont(QFont("YuGothic", 24))
        self.adressBar.returnPressed.connect(self.searchButton)
        toolbar.addWidget(self.adressBar)

        self.searchBtn = QPushButton()
        self.searchBtn.setIcon(QIcon("assets/search.svg"))
        self.searchBtn.setIconSize(QSize(36, 36))
        self.searchBtn.clicked.connect(self.searchButton)
        toolbar.addWidget(self.searchBtn)

        self.webView = QWebEngineView()
        self.setCentralWidget(self.webView)
        initialUrl = 'https://google.com'
        self.adressBar.setText(initialUrl)
        self.webView.load(QUrl(initialUrl))

    def searchButton(self):
        myUrl = self.adressBar.text()
        self.webView.load(QUrl(myUrl))

    def backButton(self):
        self.webView.back()

    def forwardButton(self):
        self.webView.forward()

    def reloadButton(self):
        self.webView.reload()

    def homeButton(self):
        self.webView.load(QUrl('https://google.com'))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())