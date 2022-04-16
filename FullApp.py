import sqlite3
from PySide2.QtCore import QPropertyAnimation, QUrl, QPoint, Qt
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from Login import Ui_Dialog
from MyMediaPlayer import Ui_MainWindow
import sys

db = sqlite3.connect('database.db')
cursor = db.cursor()
WINDOW_SIZE = 0


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
        self.ui = menu2()
        self.setupUi(self.mainMenu)

    def mousePressEvent(self, event):
        self.clickPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.isMaximized() == False:
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
            # Проверка поля ввода ("Пароль")
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
            notification = (f"Успешная регистрация аккаунта {user_login}")
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleConfirmed)
            db.commit()
        else:
            notification = 'Такая записать уже имеется!'
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
            notification = "Данная учётная запись не найдена"
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


class menu2(QtWidgets.QMainWindow, Ui_MainWindow):
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
        self.VolumeSlider.sliderMoved.connect(self.setVolume)
        # Кнопки на левом меню
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MediaPlayer))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Settings))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Information))

        def move_window(event):
            if self.isMaximized() == False:
                if event.buttons() == Qt.LeftButton:
                    delta = QPoint(event.globalPos() - self.clickPos)
                    self.move(self.x() + delta.x(), self.y() + delta.y())
                    self.clickPos = event.globalPos()

        self.main_header.mouseMoveEvent = move_window
        self.show()
        self.pushButton_3.clicked.connect(self.return_menu)

    def return_menu(self):
        self.first_window = QtWidgets.QMainWindow()
        self.ui = RegLog()
        self.setupUi(self.first_window)
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

    def setVolume(self, value):
        self.mediaPlayer.setVolume(value)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = RegLog()
    window.show()
    sys.exit(App.exec_())
