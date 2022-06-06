from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(984, 890)
        Dialog.setStyleSheet("background-color:rgb(36,41,46);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 5, 9, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.restoreBtn = QtWidgets.QPushButton(self.frame_2)
        self.restoreBtn.setMinimumSize(QtCore.QSize(0, 15))
        self.restoreBtn.setMaximumSize(QtCore.QSize(16777215, 10195))
        self.restoreBtn.setStyleSheet("QPushButton{\n"
                                      " padding:5px;\n"
                                      "border:none;\n"
                                      "border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgb(35,35,35);\n"
                                      "border:none;\n"
                                      "border-radius:10px;\n"
                                      "}")
        self.restoreBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreBtn.setIcon(icon)
        self.restoreBtn.setObjectName("restoreBtn")
        self.horizontalLayout.addWidget(self.restoreBtn)
        self.minimizeBtn = QtWidgets.QPushButton(self.frame_2)
        self.minimizeBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.minimizeBtn.setMaximumSize(QtCore.QSize(16777215, 10195))
        self.minimizeBtn.setStyleSheet("QPushButton{\n"
                                       " padding:5px;\n"
                                       "border:none;\n"
                                       "border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color:rgb(35,35,35);\n"
                                       "border:none;\n"
                                       "border-radius:10px;\n"
                                       "}")
        self.minimizeBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/minimize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeBtn.setIcon(icon1)
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout.addWidget(self.minimizeBtn)
        self.closeBtn = QtWidgets.QPushButton(self.frame_2)
        self.closeBtn.setMinimumSize(QtCore.QSize(0, 15))
        self.closeBtn.setMaximumSize(QtCore.QSize(16777215, 10195))
        self.closeBtn.setStyleSheet("QPushButton{\n"
                                    " padding:5px;\n"
                                    "border:none;\n"
                                    "border-radius:10px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:rgb(35,35,35);\n"
                                    "border:none;\n"
                                    "border-radius:10px;\n"
                                    "}")
        self.closeBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignRight)
        self.content_2 = QtWidgets.QFrame(self.widget)
        self.content_2.setMinimumSize(QtCore.QSize(0, 500))
        self.content_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_2.setObjectName("content_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.login_area_2 = QtWidgets.QFrame(self.content_2)
        self.login_area_2.setMaximumSize(QtCore.QSize(550, 650))
        self.login_area_2.setStyleSheet("")
        self.login_area_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area_2.setObjectName("login_area_2")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area_2)
        self.lineEdit_user.setGeometry(QtCore.QRect(90, 320, 421, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
                                         "    padding: 15px;\n"
                                         "    background-color: rgb(47, 54, 61);\n"
                                         "    color: rgb(235, 235, 235);\n"
                                         "    border:0px;\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    background-color:rgb(52,58,67);\n"
                                         "}\n"
                                         "QLineEdit:focus {    \n"
                                         "    background-color:rgb(58,63,72);\n"
                                         "}")
        self.lineEdit_user.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_user.setInputMask("")
        self.lineEdit_user.setMaxLength(32)
        self.lineEdit_user.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_user.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area_2)
        self.lineEdit_password.setGeometry(QtCore.QRect(90, 390, 421, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
                                             "    padding: 15px;\n"
                                             "    background-color: rgb(47, 54, 61);\n"
                                             "    color: rgb(235, 235, 235);\n"
                                             "    border:0px;\n"
                                             "}\n"
                                             "QLineEdit:hover {\n"
                                             "    background-color:rgb(52,58,67);\n"
                                             "}\n"
                                             "QLineEdit:focus {    \n"
                                             "    background-color:rgb(58,63,72);\n"
                                             "}")
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setReadOnly(False)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area_2)
        self.pushButton_login.setGeometry(QtCore.QRect(150, 520, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton {    \n"
                                            "    background-color: rgb(47,54, 61);\n"
                                            "    border: 2px solid rgb(140, 140, 140);\n"
                                            "    border-radius: 7px;\n"
                                            "    color: rgb(200, 200, 200);\n"
                                            "}\n"
                                            "QPushButton:hover {       \n"
                                            "    background-color: rgb(51, 59, 66);\n"
                                            "    border: 2px solid rgb(150, 150,150);\n"
                                            "}\n"
                                            "QPushButton:pressed {    \n"
                                            "    background-color: rgb(54, 62, 70);\n"
                                            "    border: 2px solid rgb(160, 160, 160);    \n"
                                            "    color: rgb(225, 225, 225);\n"
                                            "}")
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_reg = QtWidgets.QPushButton(self.login_area_2)
        self.pushButton_reg.setGeometry(QtCore.QRect(150, 580, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.pushButton_reg.setFont(font)
        self.pushButton_reg.setStyleSheet("QPushButton {    \n"
                                          "    background-color: rgb(47,54, 61);\n"
                                          "    border: 2px solid rgb(140, 140, 140);\n"
                                          "    border-radius: 7px;\n"
                                          "    color: rgb(200, 200, 200);\n"
                                          "}\n"
                                          "QPushButton:hover {       \n"
                                          "    background-color: rgb(51, 59, 66);\n"
                                          "    border: 2px solid rgb(150, 150,150);\n"
                                          "}\n"
                                          "QPushButton:pressed {    \n"
                                          "    background-color: rgb(54, 62, 70);\n"
                                          "    border: 2px solid rgb(160, 160, 160);    \n"
                                          "    color: rgb(225, 225, 225);\n"
                                          "}")
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.frame_error = QtWidgets.QFrame(self.login_area_2)
        self.frame_error.setGeometry(QtCore.QRect(40, 300, 501, 141))
        self.frame_error.setStyleSheet("background-color:rgb(255,0,0);")
        self.frame_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setGeometry(QtCore.QRect(80, 40, 361, 51))
        self.label_error.setStyleSheet("color: rgb(25, 25, 25);\n"
                                       "font: 9pt \"MS Shell Dlg 2\";")
        self.label_error.setScaledContents(False)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.pushButton_close_popup = QtWidgets.QPushButton(self.frame_error)
        self.pushButton_close_popup.setGeometry(QtCore.QRect(450, 60, 20, 20))
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
        self.pushButton_close_popup.setIcon(icon2)
        self.pushButton_close_popup.setObjectName("pushButton_close_popup")
        self.pushButton_user = QtWidgets.QPushButton(self.login_area_2)
        self.pushButton_user.setEnabled(True)
        self.pushButton_user.setGeometry(QtCore.QRect(40, 320, 51, 50))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.pushButton_user.setFont(font)
        self.pushButton_user.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_user.setStyleSheet("QPushButton {    \n"
                                           "    background-color: rgb(59,67, 74);\n"
                                           "    border: 0px solid rgb(140, 140, 140);\n"
                                           "    border-radius: 0px;\n"
                                           "    color: rgb(200, 200, 200);\n"
                                           "}\n"
                                           "")
        self.pushButton_user.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_user.setIcon(icon3)
        self.pushButton_user.setIconSize(QtCore.QSize(27, 27))
        self.pushButton_user.setObjectName("pushButton_user")
        self.pushButton_pass = QtWidgets.QPushButton(self.login_area_2)
        self.pushButton_pass.setEnabled(True)
        self.pushButton_pass.setGeometry(QtCore.QRect(40, 390, 51, 50))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.pushButton_pass.setFont(font)
        self.pushButton_pass.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_pass.setStyleSheet("QPushButton {    \n"
                                           "    background-color: rgb(59,67, 74);\n"
                                           "    border: 0px solid rgb(140, 140, 140);\n"
                                           "    border-radius: 0px;\n"
                                           "    color: rgb(200, 200, 200);\n"
                                           "}\n"
                                           "")
        self.pushButton_pass.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/lock (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_pass.setIcon(icon4)
        self.pushButton_pass.setIconSize(QtCore.QSize(27, 27))
        self.pushButton_pass.setObjectName("pushButton_pass")
        self.pushButton = QtWidgets.QPushButton(self.login_area_2)
        self.pushButton.setGeometry(QtCore.QRect(350, 120, 91, 131))
        self.pushButton.setStyleSheet("QPushButton {    \n"
                                      "    background-color:rgb(36,41,46);\n"
                                      "    border: 0px solid rgb(140, 140, 140);\n"
                                      "    border-radius: 0px;\n"
                                      "    color: rgb(200, 200, 200);\n"
                                      "}\n"
                                      "")
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/gitlab.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(84, 84))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.login_area_2)
        self.label.setGeometry(QtCore.QRect(90, 150, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255,255,255)")
        self.label.setObjectName("label")
        self.lineEdit_user.raise_()
        self.lineEdit_password.raise_()
        self.pushButton_login.raise_()
        self.pushButton_reg.raise_()
        self.pushButton_user.raise_()
        self.pushButton_pass.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.frame_error.raise_()
        self.horizontalLayout_4.addWidget(self.login_area_2)
        self.verticalLayout_2.addWidget(self.content_2)
        self.bottom_2 = QtWidgets.QFrame(self.widget)
        self.bottom_2.setMinimumSize(QtCore.QSize(0, 100))
        self.bottom_2.setMaximumSize(QtCore.QSize(100000, 20))
        self.bottom_2.setStyleSheet("background-color:rgb(30,32,37);")
        self.bottom_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_2.setObjectName("bottom_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.bottom_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, 9)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_credits_2 = QtWidgets.QLabel(self.bottom_2)
        self.label_credits_2.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits_2.setFont(font)
        self.label_credits_2.setStyleSheet("color:rgb(210,210,210)")
        self.label_credits_2.setObjectName("label_credits_2")
        self.horizontalLayout_6.addWidget(self.label_credits_2, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.bottom_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_user.setPlaceholderText(_translate("Dialog", "ПОЛЬЗОВАТЕЛЬ"))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog", "ПАРОЛЬ"))
        self.pushButton_login.setText(_translate("Dialog", "ВОЙТИ"))
        self.pushButton_reg.setText(_translate("Dialog", "РЕГИСТРАЦИЯ"))
        self.label_error.setText(_translate("Dialog", "Ошибка!\n"
                                                      " Попробуйте снова"))
        self.label.setText(_translate("Dialog", "MediaPlayer"))
        self.label_credits_2.setText(_translate("Dialog", "GITHUB:thug-cawa\n"
                                                          "GITFLIC:@cawa"))
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_error.hide())
        self.frame_error.hide()
        # Создание 2 переменных для изменения цвета уведомления
        self.styleError = ("background-color: rgb(255, 0,0);")
        self.styleConfirmed = ("background-color: rgb(39, 203,20);")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
