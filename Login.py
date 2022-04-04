from PyQt5 import QtCore, QtGui, QtWidgets
import files_rc



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 813)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/Icon/TESTui/images/house_navigation_button_app_page_dashboard_home_icon_219341.ico"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
                                 "background-color: rgb(35, 35,35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 650))
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
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb(139, 0, 0);\n"
                                         "    border-radius: 15px;\n"
                                         "    padding: 15px;\n"
                                         "    background-color: rgb(10, 10, 10);\n"
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
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
                                             "    border: 2px solid rgb(139, 0, 0);\n"
                                             "    border-radius: 15px;\n"
                                             "    padding: 15px;\n"
                                             "    background-color: rgb(10, 10, 10);    \n"
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
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.checkBox_save_user.setFont(font)
        self.checkBox_save_user.setStyleSheet("QCheckBox::indicator {\n"
                                              "    border: 2px solid rgb(100, 100, 100);\n"
                                              "    width: 15px;\n"
                                              "    height: 15px;\n"
                                              "    border-radius: 5px;    \n"
                                              "    background-color: rgb(35, 35, 35);\n"
                                              "}\n"
                                              "QCheckBox::indicator:checked {\n"
                                              "    border: 2px solid rgb(139, 0, 0);\n"
                                              "    background-color: rgb(255, 0, 0);\n"
                                              "}")
        self.checkBox_save_user.setObjectName("checkBox_save_user")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area)
        self.pushButton_login.setGeometry(QtCore.QRect(85, 480, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton {    \n"
                                            "    background-color: rgb(10,10, 10);\n"
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
        self.pushButton_reg = QtWidgets.QPushButton(self.login_area)
        self.pushButton_reg.setGeometry(QtCore.QRect(85, 425, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(9)
        self.pushButton_reg.setFont(font)
        self.pushButton_reg.setStyleSheet("QPushButton {    \n"
                                          "    background-color: rgb(10,10, 10);\n"
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
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.frame_error = QtWidgets.QFrame(self.login_area)
        self.frame_error.setGeometry(QtCore.QRect(0, 200, 450, 101))
        self.frame_error.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                       "border-radius: 5px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setEnabled(True)
        self.label_error.setGeometry(QtCore.QRect(60, 10, 341, 81))
        self.label_error.setStyleSheet("color: rgb(35, 35, 35);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";")
        self.label_error.setScaledContents(False)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.pushButton_close_popup = QtWidgets.QPushButton(self.frame_error)
        self.pushButton_close_popup.setGeometry(QtCore.QRect(420, 10, 20, 20))
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
        self.pushButton_close_popup.setObjectName("pushButton_close_popup")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_credits = QtWidgets.QLabel(self.bottom)
        self.label_credits.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_credits.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_4.addWidget(self.label_credits)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "ПОЛЬЗОВАТЕЛЬ"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "ПАРОЛЬ"))
        self.checkBox_save_user.setText(_translate("MainWindow", "Запомнить пользователя"))
        self.pushButton_login.setText(_translate("MainWindow", "ВОЙТИ"))
        self.pushButton_reg.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ"))
        self.label_error.setText(_translate("MainWindow", "Ошибка!\n"
                                                          " Попробуйте снова"))
        self.label_credits.setText(_translate("MainWindow", "CREATED BY GITHUB: thug-cawa\n"
                                                            "GITFLIC: @cawa"))
        #Кнопка закрытия уведомления
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_error.hide())
        self.frame_error.hide()
        #Создания 2 переменных для изменения цвета уведомления
        self.styleError = ("background-color: rgb(255, 0,0);")
        self.styleConfirmed = ("background-color: rgb(39, 203,20);")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())