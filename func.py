import untitled
from PyQt5 import QtWidgets
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QUrl


class VideoPlayer(QtWidgets.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.widget)
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.play_video)
        self.horizontalSlider.sliderMoved.connect(self.set_position)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.horizontalSlider_2.sliderMoved.connect(self.set_volume)

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
        self.horizontalSlider.setValue(position)

    def duration_changed(self,duration):
        self.horizontalSlider.setRange(0,duration)

    def set_volume(self):
        value = self.horizontalSlider_2.value()
        self.mediaPlayer.setVolume(value)
        self.statusBar.showMessage("Громкость " + str(value))

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = VideoPlayer()
    window.show()
    app.exec_()
