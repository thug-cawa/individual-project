from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    #Функционал
    def check_input_area(self):
        user=[]
        password=[]
        def show_notification(notification):
            self.frame_error.show()
            self.label_error.setText(notification)
        #Проверка поля ввода ("Пользователь")
        if self.lineEdit_user.text():
            user = ''
        else:
            user = "Проверьте правильность ввода Пользователь"
        #Проверка поля ввода ("Пароль")
        if self.lineEdit_password.text():
            password = ''
        else:
            password = "Проверьте правильность ввода Пароль"
        #Проверка двух полей для вывода сообщения
        if password and user != '':
            notification = "Проверьте правильность ввода двух полей"
            show_notification(notification)
        elif password + user != '':
            notification = user + password
            show_notification(notification)
        else:
            notification = "Login confirmed"
            show_notification(notification)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 783)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/Icon/TESTui/images/house_navigation_button_app_page_dashboard_home_icon_219341.ico"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
                                 "background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                       "border-radius: 5px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("color: rgb(35, 35, 35);\n"
                                       "font: 9pt \"MS Shell Dlg 2\";")
        self.label_error.setScaledContents(False)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.pushButton_close_popup = QtWidgets.QPushButton(self.frame_error)
        self.pushButton_close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet("QPushButton {\n"
                                                  "    border-radius: 5px;    \n"
                                                  "    background-image: url(:/Close_Image/TESTui/images/cil-x.png);\n"
                                                  "    background-position: center;    \n"
                                                  "    background-color: rgb(60, 60, 60);\n"
                                                  "}\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: rgb(50, 50, 50);    \n"
                                                  "    color: rgb(200, 200, 200);\n"
                                                  "}\n"
                                                  "QPushButton:pressed {\n"
                                                  "    background-color: rgb(35, 35, 35);    \n"
                                                  "    color: rgb(200, 200, 200);\n"
                                                  "}")

        self.pushButton_close_popup.setText("")
        self.pushButton_close_popup.setObjectName("pushButton_close_pupup")
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(100, 40, 251, 90))
        self.logo.setStyleSheet("\n"
                                "QFrame {\n"
                                "    background-image: url(:/Logo/TESTui/images/423.png);\n"
                                "    background-repeat: no-repeat;\n"
                                "    background-position: center;\n"
                                "    border-radius: 60px;\n"
                                "    border: 3px solid rgb(139, 0, 0);\n"
                                "    background-position: center;\n"
                                "}\n"
                                "QFrame:hover {\n"
                                "    border: 3px solid rgb(255, 0, 0);\n"
                                "}\n"
                                "\n"
                                "")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.avatar = QtWidgets.QFrame(self.login_area)
        self.avatar.setGeometry(QtCore.QRect(160, 150, 120, 120))
        self.avatar.setStyleSheet("QFrame {\n"
                                  "    background-image:url(:/Ava/TESTui/images/4232.png);\n"
                                  "    border-radius: 60px;\n"
                                  "    border: 7px solid rgb(139, 0, 0);\n"
                                  "    background-position: center;\n"
                                  "}\n"
                                  "QFrame:hover {\n"
                                  "    border: 7px solid rgb(255, 0, 0);\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setObjectName("avatar")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_user.setGeometry(QtCore.QRect(85, 288, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb(139, 0, 0);\n"
                                         "    border-radius: 15px;\n"
                                         "    padding: 15px;\n"
                                         "    background-color: rgb(35, 35, 35);\n"
                                         "    color: rgb(255, 0, 0);\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(255, 0, 0);\n"
                                         "}\n"
                                         "QLineEdit:focus {\n"
                                         "    border: 2px solid rgb(255, 0, 0);    \n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "}")
        self.lineEdit_user.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_user.setInputMask("")
        self.lineEdit_user.setMaxLength(32)
        self.lineEdit_user.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_user.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(85, 340, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
                                             "    border: 2px solid rgb(139, 0, 0);\n"
                                             "    border-radius: 15px;\n"
                                             "    padding: 15px;\n"
                                             "    background-color: rgb(35, 35, 35);    \n"
                                             "    color: rgb(255, 0, 0);\n"
                                             "}\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 2px solid rgb(255, 0, 0);\n"
                                             "}\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 2px solid rgb(255, 0, 0);    \n"
                                             "    color: rgb(200, 200, 200);\n"
                                             "}")
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setReadOnly(False)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.checkBox_save_user = QtWidgets.QCheckBox(self.login_area)
        self.checkBox_save_user.setGeometry(QtCore.QRect(85, 395, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.checkBox_save_user.setFont(font)
        self.checkBox_save_user.setStyleSheet("QCheckBox::indicator {\n"
                                              "    border: 3px solid rgb(100, 100, 100);\n"
                                              "    width: 15px;\n"
                                              "    height: 15px;\n"
                                              "    border-radius: 10px;    \n"
                                              "    background-color: rgb(35, 35, 35);\n"
                                              "}\n"
                                              "QCheckBox::indicator:checked {\n"
                                              "    border: 3px solid rgb(139, 0, 0);\n"
                                              "    background-color: rgb(255, 0, 0);\n"
                                              "}")
        self.checkBox_save_user.setObjectName("checkBox_save_user")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area)
        self.pushButton_login.setGeometry(QtCore.QRect(85, 425, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton {    \n"
                                            "    background-color: rgb(35,35, 35);\n"
                                            "    border: 2px solid rgb(139, 0, 0);\n"
                                            "    border-radius: 15px;\n"
                                            "    color: rgb(139, 0, 0);\n"
                                            "}\n"
                                            "QPushButton:hover {    \n"
                                            "    \n"
                                            "    background-color: rgb(39, 39, 39);\n"
                                            "    border: 2px solid rgb(255, 0, 0);\n"
                                            "}\n"
                                            "QPushButton:pressed {    \n"
                                            "    background-color: rgb(255, 0, 0);\n"
                                            "    border: 2px solid rgb(139, 0, 0);    \n"
                                            "    color: rgb(35, 35, 35);\n"
                                            "}\n"
                                            "\n"
                                            "")
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 45))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_developer = QtWidgets.QLabel(self.bottom)
        self.label_developer.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_developer.setFont(font)
        self.label_developer.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_developer.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_developer.setObjectName("label_credits")
        self.horizontalLayout_4.addWidget(self.label_developer)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Функционал
        #Кнопка закрытия окна ошибки
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_error.hide())
        self.frame_error.hide()
        #Кнопка Логин
        self. pushButton_login.clicked.connect(self.check_input_area)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_error.setText(_translate("MainWindow", "Ошибка!\n"
                                                          " Попробуйте снова"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "ПОЛЬЗОВАТЕЛЬ"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "ПАРОЛЬ"))
        self.checkBox_save_user.setText(_translate("MainWindow", "Запомнить пользователя"))
        self.pushButton_login.setText(_translate("MainWindow", "ВОЙТИ"))
        self.label_developer.setText(_translate("MainWindow", "GITHUB:thug-cawa\n"
                                                            "GITFLIC:@cawa"))


import files_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
