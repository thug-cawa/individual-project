import sqlite3
from PySide2 import QtCore, QtGui, QtWidgets
from Login import Ui_Dialog
from PySide2.QtCore import QPoint,Qt

db = sqlite3.connect('database.db')
cursor = db.cursor()
WINDOW_SIZE = 0


class RegLog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(RegLog, self).__init__()
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_reg.clicked.connect(self.reg)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.restoreBtn.clicked.connect(lambda: self.showMinimized())
        self.minimizeBtn.clicked.connect(lambda: self.restore_or_maximize_window())
        self.closeBtn.clicked.connect(lambda: self.close())
        self.show()

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

    #Регистрация
    def reg(self):
        def show_notification(notification):
            self.frame_error.show()
            self.label_error.setText(notification)
        user_login = self.lineEdit_user.text()
        user_password = self.lineEdit_password.text()
        user = ''
        password = ''
        #Проверяем заполнены ли все поля
        if self.lineEdit_user.text():
           user = ''
        else:
           user = "Проверьте правильность ввода Пользователь"
            #Проверка поля ввода ("Пароль")
        if self.lineEdit_password.text():
            password = ''
        else:
            password = "Проверьте правильность ввода Пароль"
            #Проверка двух полей
        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if password and user != '':
                notification = "Проверьте правильность ввода двух полей"
                show_notification(notification)
                self.frame_error.setStyleSheet(self.styleError)
        elif password + user != '':
                notification = user + password
                show_notification(notification)
                self.frame_error.setStyleSheet(self.styleError)

        #Проверяем есть ли такой аккаунт в базе,если нет запись
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
    #Логин
    def login(self):
        def show_notification(notification):
            self.frame_error.show()
            self.label_error.setText(notification)
        user_login = self.lineEdit_user.text()
        user_password = self.lineEdit_password.text()
        user = ''
        password = ''
        #Достаём логин и пароль из базы для последующей проверки
        query = 'SELECT password,login FROM users WHERE login =\'' + user_login + "\'"
        cursor.execute(query)
        result_pass = cursor.fetchall()
        #Проверяем заполнены ли все поля
        if self.lineEdit_user.text():
            user = ''
        else:
            user = "Проверьте правильность ввода Пользователь"
            #Проверка поля ввода ("Пароль")
        if self.lineEdit_password.text():
            password = ''
        else:
            password = "Проверьте правильность ввода Пароль"
            #Проверка двух полей
        if password and user != '':
            notification = "Проверьте правильность ввода двух полей"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)
        elif password + user != '':
            notification = user + password
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)
        #Проверка на правильность ввода логина и пароля
        elif result_pass == []:
            notification = "Данная учётная запись не найдена"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)
            return
        elif result_pass[0][0] == user_password and result_pass[0][1] == user_login:
            notification = "Вы успешно авторизовались"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleConfirmed)
        else:
            notification = "Неправильный пароль"
            show_notification(notification)
            self.frame_error.setStyleSheet(self.styleError)
        print(result_pass)
        print(user_password)


import sys
App = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
window = RegLog()
window.show()
sys.exit(App.exec_())