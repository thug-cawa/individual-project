import sqlite3
from PyQt5.QtCore import QPropertyAnimation, QUrl, QPoint, Qt,QEvent,QRect,QThread,pyqtSignal,QObject
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from Login import Ui_Dialog
from MyMediaPlayer import Ui_MainWindow
from VideoWidget import Ui_Form
from yt_downloader import Ui_MainWindow2
import sys
import os
import sys
import requests
import time
import traceback
from pytube import YouTube


db = sqlite3.connect('database.db')
cursor = db.cursor()
WINDOW_SIZE = 0
WINDOW_SIZE2 = 0


class RegLog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_reg.clicked.connect(self.reg)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.restoreBtn.clicked.connect(lambda: self.showMinimized())
        self.minimizeBtn.clicked.connect(lambda: self.restore_or_maximize_window())
        self.closeBtn.clicked.connect(lambda: self.close())
        self.show()

    def main_menu(self):
        self.mainMenu = QtWidgets.QMainWindow()
        self.ui = Menu()
        self.setupUi(self.mainMenu)

    def mousePressEvent(self, event):
        self.clickPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if not self.isMaximized():
            if event.buttons() == Qt.LeftButton:
                delta = QPoint(event.globalPos() - self.clickPos)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.clickPos = event.globalPos()

    def restore_or_maximize_window(self):
        global WINDOW_SIZE
        win_stat = WINDOW_SIZE
        if win_stat == 0:
            WINDOW_SIZE = 1
            self.showMaximized()
        else:
            WINDOW_SIZE = 0
            self.showNormal()

    # Регистрация
    def reg(self):
        def show_notification(notification):
            self.frame_error.show()
            self.label_error.setText(notification)

        user_login = self.lineEdit_user.text()
        user_password = self.lineEdit_password.text()
        user = ''
        password = ''
        # Проверяем заполнены ли все поля
        if self.lineEdit_user.text():
            user = ''
        else:
            user = "Проверьте правильность ввода Пользователь"
        # Проверка поля ввода("Пароль")
        if self.lineEdit_password.text():
            password = ''
        else:
            password = "Проверьте правильность ввода Пароль"
            # Проверка двух полей
        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if password and user != '':
            notification = "Проверьте правильность ввода двух полей"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)
        elif password + user != '':
            notification = user + password
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)

        # Проверяем есть ли такой аккаунт в базе,если нет запись
        elif cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES ("{user_login}", "{user_password}")')
            notification = (f'Успешная регистрация аккаунта {user_login}')
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleConfirmed)
            db.commit()
        else:
            notification = 'Такая запись уже имеется!'
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)

    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    # Логин
    def login(self):
        def show_notification(notification):
            self.frame_error.show()
            self.label_error.setText(notification)

        user_login = self.lineEdit_user.text()
        user_password = self.lineEdit_password.text()
        user = ''
        password = ''
        # Достаём логин и пароль из базы для последующей проверки
        query = 'SELECT password,login FROM users WHERE login =\'' + user_login + "\'"
        cursor.execute(query)
        result_pass = cursor.fetchall()
        # Проверяем заполнены ли все поля
        if self.lineEdit_user.text():
            user = ''
        else:
            user = "Проверьте правильность ввода Пользователь"
            # Проверка поля ввода ("Пароль")
        if self.lineEdit_password.text():
            password = ''
        else:
            password = "Проверьте правильность ввода Пароль"
            # Проверка двух полей
        if password and user != '':
            notification = "Проверьте правильность ввода двух полей"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)
        elif password + user != '':
            notification = user + password
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)
        # Проверка на правильность ввода логина и пароля
        elif result_pass == []:
            notification = "Такого аккаунта нет"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)
            return
        elif result_pass[0][0] == user_password and result_pass[0][1] == user_login:
            notification = "Вы успешно авторизовались"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleConfirmed)
            self.main_menu()
            self.close()
        else:
            notification = "Неправильный пароль"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)



class Menu(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
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
        self.stackedWidget.setCurrentWidget(self.MediaPlayer)
        self.VolumeSlider.sliderMoved.connect(self.set_volume)
        # Кнопки на левом меню
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MediaPlayer))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Settings))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Information))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.YouTube))
        self.pushButton_8.clicked.connect(self.ytdownloader_menu)


        def move_window(event):
            if not self.isMaximized():
                if event.buttons() == Qt.LeftButton:
                    delta = QPoint(event.globalPos() - self.clickPos)
                    self.move(self.x() + delta.x(), self.y() + delta.y())
                    self.clickPos = event.globalPos()

        self.main_header.mouseMoveEvent = move_window
        self.show()
        self.pushButton_3.clicked.connect(self.return_menu)
        self.show()
        self.pushButton_7.clicked.connect(self.open_player)
    def ytdownloader_menu(self):
        self.yt_window = QtWidgets.QMainWindow()
        self.ui = Window()
        self.close()

    def return_menu(self):
        self.first_window = QtWidgets.QMainWindow()
        self.ui = RegLog()
        self.setupUi(self.first_window)
        self.close()

    def open_player(self):
        self.second_player = QtWidgets.QMainWindow()
        self.ui = Video_Widg()
        self.setupUi(self.second_player)
        self.close()

    def mousePressEvent(self, event):
        self.clickPos = event.globalPos()

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
            new_width = 200
        else:
            new_width = 0
        self.animation = QPropertyAnimation(self.left_side_menu, b'minimumWidth')
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Video")
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

    def set_volume(self, value):
        self.mediaPlayer.setVolume(value)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


class Video_Widg(QtWidgets.QDialog,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.dragPos = QtCore.QPoint()
        self.mediaPlayer.setVideoOutput(self.widget_2)
        self.OpenButton.clicked.connect(self.open_file)
        self.PlayButton.clicked.connect(self.play_video)
        self.VideoSlider.sliderMoved.connect(self.set_position)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.VolumeSlider.sliderMoved.connect(self.set_volume)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(lambda : self.restore_or_maximize_window())
        self.pushButton_2.clicked.connect(self.main_menu)
        self.show()
        self.installEventFilter(self)


        def move_window(event):
            if not self.isFullScreen():
                if event.buttons() == Qt.LeftButton:
                    delta = QPoint(event.globalPos() - self.clickPos)
                    self.move(self.x() + delta.x(), self.y() + delta.y())
                    self.clickPos = event.globalPos()


        self.frame_2.mouseMoveEvent = move_window



    def restore_or_maximize_window(self):
        global WINDOW_SIZE2
        win_stat = WINDOW_SIZE2
        if win_stat == 0:
            WINDOW_SIZE2 = 1
            self.showFullScreen()
            self.hide_taskbar()
        else:
            WINDOW_SIZE2 = 0
            self.showNormal()
            self.unhide_taskbar()

    def mousePressEvent(self, event):
        self.clickPos = event.globalPos()


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.pushButton_2.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def main_menu(self):
        self.mainMenu = QtWidgets.QMainWindow()
        self.ui = Menu()
        self.setupUi(self.mainMenu)
        self.close()

    def position_changed(self, position):
        self.VideoSlider.setValue(position)

    def duration_changed(self, duration):
        self.VideoSlider.setRange(0, duration)

    def set_volume(self, value):
        self.mediaPlayer.setVolume(value)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

class ProcuradorDeVideos(QObject):
    finished = pyqtSignal()
    def achar_video(self):
        try:
            yt = YouTube(self.tela.lineEdit.text())
            response = requests.get(yt.thumbnail_url)
            nome = "video_thumb.jpg"
            with open("video_thumb.jpg", "wb") as thumbnail:
                thumbnail.write(response.content)
            pix = QPixmap(nome)
            self.tela.label_6.setPixmap(pix)
            self.tela.stackedWidget.setCurrentIndex(0)
            self.tela.label_13.setText(str(yt.title))
            self.tela.label_15.setText(f"Продолжительность: {str(time.strftime('%H:%M:%S', time.gmtime(int(yt.length))))}")
        except Exception as e:
            print(traceback.format_exc())
        self.finished.emit()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.setup_program_ui()
        self.show()

    def setup_program_ui(self):
        self.ui.label_13.setText("")
        self.ui.label_11.setText("YOUTUBE DOWNLOADER 2022")
        self.ui.label_11.setStyleSheet("font-size: 16px;color:white")
        self.ui.pushButton_2.clicked.connect(lambda: self.threads_video())
        self.ui.pushButton.clicked.connect(lambda: self.select_directory())
        self.ui.pushButton_5.clicked.connect(lambda: self.download("mp3"))
        self.ui.pushButton_3.clicked.connect(lambda: self.download("mp4 hd"))
        self.ui.pushButton_4.clicked.connect(lambda: self.download("mp4 low"))
        self.ui.pushButton_6.clicked.connect(self.main_menu)
        self.show()

    def main_menu(self):
        self.mainMenu = QtWidgets.QMainWindow()
        self.ui = Menu()
        self.close()


    def download(self, tipo_download):
        try:
            yt = YouTube(str(self.ui.lineEdit.text()))
        except:
            QtWidgets.QMessageBox.about(self,
                                        'Erro', 'Неправильная ссылка')
            return

        path_download = self.ui.label_12.text()

        if path_download == "":
            QtWidgets.QMessageBox.about(self,
                                        'Erro', 'Перед загрузкой выберите папку назначения')
            return

        if not os.path.exists(path_download):
            QtWidgets.QMessageBox.about(self,
                                        'Erro', 'Указанный путь загрузки неверный.')
            return
        self.ui.label_13.setText("Загрузка видео...")

        if tipo_download == "mp3":
            self.donwload_mp3(yt, path_download)
        if tipo_download == "mp4 hd":
            self.donwload_mp4(yt, path_download, "MAX")
        if tipo_download == "mp4 low":
            self.donwload_mp4(yt, path_download, "MIN")

        self.ui.label_13.setText(str(yt.title))

    def donwload_mp4(self, obj_youtube, path_download, qualidade):
        if qualidade == "MAX":
            video_te = obj_youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if qualidade == "MIN":
            video_te = obj_youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first()

        video_te.download(filename=f"{obj_youtube.title}_{video_te.resolution}.mp4".replace("|", ""),
                           output_path=path_download)
        QtWidgets.QMessageBox.about(self,
                                    'Успешшно', f'Видео загружено в каталог "{path_download}"')
        return

    def donwload_mp3(self, obj_youtube, path_download):
        video = obj_youtube.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=path_download)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        QtWidgets.QMessageBox.about(self,
                                    'Успешно', f'Видео загружено в каталог: "{path_download}"')
        return

    def select_directory(self):
        diretorio = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               'Выберите папку в котором будет сохранён:', 'C:\\',
                                                               QtWidgets.QFileDialog.ShowDirsOnly)

        if not diretorio:
            return
        if diretorio.upper() == "C:/":
            QtWidgets.QMessageBox.about(self,
                                        'Ошибка',
                                        'Не стоит указывать путь "C:/"')
            return
        self.ui.label_12.setText(diretorio)

    def threads_video(self):
        self.thread = QThread()
        self.procurador = ProcuradorDeVideos()
        self.procurador.moveToThread(self.thread)
        self.procurador.tela = self.ui
        self.thread.started.connect(self.procurador.achar_video)
        self.procurador.finished.connect(self.thread.quit)
        self.procurador.finished.connect(self.procurador.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        self.ui.pushButton_2.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.ui.pushButton_2.setEnabled(True))

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = RegLog()
    window.show()
    sys.exit(App.exec_())
