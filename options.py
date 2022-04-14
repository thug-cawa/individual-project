from PySide2.QtCore import QPropertyAnimation, QUrl
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from MyMediaPlayer import Ui_MainWindow
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent

WINDOW_SIZE = 0


class menu2(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(menu2, self).__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.restoreBtn.clicked.connect(lambda: self.showMinimized())
        self.minimizeBtn.clicked.connect(lambda: self.restore_or_maximize_window())
        self.closeBtn.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(lambda: self.slide_left_menu())
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.widget_2)
        self.OpenButton.clicked.connect(self.open_file)
        self.PlayButton.clicked.connect(self.play_video)
        self.VideoSlider.sliderMoved.connect(self.set_position)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.VolumeSlider.sliderMoved.connect(self.set_volume)
        self.stackedWidget.setCurrentWidget(self.MediaPlayer)
        #Кнопки на левом меню
        self.pushButton_2.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.MediaPlayer))
        self.pushButton_5.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.Settings))
        self.pushButton_4.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.Information))
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
        if win_stat == 0:
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
        self.animation = QPropertyAnimation(self.left_side_menu, b'minimumWidth')
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.pushButton_2.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def position_changed(self, position):
        self.VideoSlider.setValue(position)

    def duration_changed(self, duration):
        self.VideoSlider.setRange(0, duration)

    def set_volume(self):
        value = self.VolumeSlider.value()
        self.mediaPlayer.setVolume(value)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


if __name__ == "__main__":
    import sys

    App = QtWidgets.QApplication(sys.argv)
    window = menu2()
    window.show()
    sys.exit(App.exec_())
