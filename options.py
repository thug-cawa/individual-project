from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtWidgets import *
from menu import Ui_MainWindow
WINDOW_SIZE = 0
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.minimizeBtn.clicked.connect(lambda:self.showMinimized())
        self.restoreBtn.clicked.connect(lambda: self.restore_or_maximize_window())
        self.closeBtn.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(lambda:self.slide_left_menu())
        self.show()

        def move_window(event):
            if self.isMaximized() == False:
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos
                    event.accept()

        self.main_header.mouseMoveEvent = move_window
    def restore_or_maximize_window(self):
        global WINDOW_SIZE
        win_stat = WINDOW_SIZE
        if win_stat  == 0:
            WINDOW_SIZE = 1
            self.showMaximized()
        else:
            WINDOW_SIZE = 0
            self.showNormal()
    def slide_left_menu(self):
        width = self.left_side_menu.width()
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self.left_side_menu,b'minimumWidth')
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()




    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()




import sys
App = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(App.exec_())