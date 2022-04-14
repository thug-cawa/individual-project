from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 716)
        MainWindow.setStyleSheet("QPushButton:hover {    \n"
"    background-color: rgb(39, 39, 39);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_header = QtWidgets.QFrame(self.widget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 80))
        self.main_header.setStyleSheet("background-color:#16191d;")
        self.main_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_bar_container = QtWidgets.QFrame(self.main_header)
        self.title_bar_container.setMinimumSize(QtCore.QSize(0, 40))
        self.title_bar_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar_container.setObjectName("title_bar_container")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_menu_toggle = QtWidgets.QFrame(self.title_bar_container)
        self.left_menu_toggle.setMinimumSize(QtCore.QSize(400, 25))
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.left_menu_toggle.setStyleSheet("background-color:#16191d;")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.pushButton = QtWidgets.QPushButton(self.left_menu_toggle)
        self.pushButton.setGeometry(QtCore.QRect(10, 5, 45, 35))
        self.pushButton.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(45, 16777215))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"padding-left:15px;\n"
"background-position:center left;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(15,15,15);\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../TESTui/images/menu (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.left_menu_toggle, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addWidget(self.title_bar_container, 0, QtCore.Qt.AlignLeft)
        self.top_right_btns = QtWidgets.QFrame(self.main_header)
        self.top_right_btns.setMinimumSize(QtCore.QSize(0, 30))
        self.top_right_btns.setMaximumSize(QtCore.QSize(131, 16777215))
        self.top_right_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_right_btns.setObjectName("top_right_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.restoreBtn = QtWidgets.QPushButton(self.top_right_btns)
        self.restoreBtn.setMinimumSize(QtCore.QSize(0, 15))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../TESTui/images/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreBtn.setIcon(icon1)
        self.restoreBtn.setObjectName("restoreBtn")
        self.horizontalLayout_3.addWidget(self.restoreBtn, 0, QtCore.Qt.AlignTop)
        self.minimizeBtn = QtWidgets.QPushButton(self.top_right_btns)
        self.minimizeBtn.setMinimumSize(QtCore.QSize(0, 15))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../TESTui/images/minimize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeBtn.setIcon(icon2)
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_3.addWidget(self.minimizeBtn, 0, QtCore.Qt.AlignTop)
        self.closeBtn = QtWidgets.QPushButton(self.top_right_btns)
        self.closeBtn.setMinimumSize(QtCore.QSize(0, 15))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../TESTui/images/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon3)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_3.addWidget(self.closeBtn, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.top_right_btns)
        self.verticalLayout_2.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.widget)
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(self.main_body)
        self.left_side_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.left_side_menu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.left_side_menu.setStyleSheet("background-color:#16191d;;")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.left_menu_buttons = QtWidgets.QFrame(self.left_side_menu)
        self.left_menu_buttons.setMinimumSize(QtCore.QSize(0, 45))
        self.left_menu_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_buttons.setObjectName("left_menu_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_buttons)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.left_menu_buttons)
        self.pushButton_2.setMinimumSize(QtCore.QSize(175, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"padding-left:15px;\n"
"background-position:center left;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(15,15,15);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../TESTui/images/youtube.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.left_menu_buttons)
        self.pushButton_5.setMinimumSize(QtCore.QSize(175, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"padding-left:15px;\n"
"background-position:center left;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(15,15,15);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../TESTui/images/settings (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_5)
        self.verticalLayout_3.addWidget(self.left_menu_buttons)
        self.pushButton_4 = QtWidgets.QPushButton(self.left_side_menu)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"padding-left:15px;\n"
"background-position:center left;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(15,15,15);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../TESTui/images/github (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.left_side_menu)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"padding-left:15px;\n"
"background-position:center left;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(15,15,15);\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../TESTui/images/log-out (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(self.main_body)
        self.center_main_items.setStyleSheet("background-color:#2c313c;")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.center_main_items)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName("stackedWidget")
        self.MediaPlayer = QtWidgets.QWidget()
        self.MediaPlayer.setObjectName("MediaPlayer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MediaPlayer)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QVideoWidget(self.MediaPlayer)
        self.widget_2.setMinimumSize(QtCore.QSize(1000, 575))
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4.addWidget(self.widget_2)
        self.frame = QtWidgets.QFrame(self.MediaPlayer)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.OpenButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenButton.sizePolicy().hasHeightForWidth())
        self.OpenButton.setSizePolicy(sizePolicy)
        self.OpenButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.OpenButton.setFont(font)
        self.OpenButton.setStyleSheet("QPushButton {    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35,35, 35);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"")
        self.OpenButton.setObjectName("OpenButton")
        self.horizontalLayout_7.addWidget(self.OpenButton)
        self.PlayButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayButton.sizePolicy().hasHeightForWidth())
        self.PlayButton.setSizePolicy(sizePolicy)
        self.PlayButton.setMinimumSize(QtCore.QSize(0, 25))
        self.PlayButton.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(35,35, 35);\n"
"    border-radius:10px;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover {    \n"
"  background-color:rgb(55,55,55)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 35, 35);    \n"
"}\n"
"\n"
"")
        self.PlayButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../TESTui/images/play (2).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayButton.setIcon(icon8)
        self.PlayButton.setIconSize(QtCore.QSize(20, 16))
        self.PlayButton.setObjectName("PlayButton")
        self.horizontalLayout_7.addWidget(self.PlayButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.VideoSlider = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoSlider.sizePolicy().hasHeightForWidth())
        self.VideoSlider.setSizePolicy(sizePolicy)
        self.VideoSlider.setMinimumSize(QtCore.QSize(0, 25))
        self.VideoSlider.setStyleSheet("QSlider {    \n"
"    background-color: rgb(35,35, 35);;\n"
"    border-radius: 10px;\n"
"    color: rgb(139, 0, 0);\n"
"}\n"
"QSlider:hover {    \n"
"    background-color: rgb(55, 55, 55);\n"
"}")
        self.VideoSlider.setMaximum(100)
        self.VideoSlider.setProperty("value", 0)
        self.VideoSlider.setSliderPosition(0)
        self.VideoSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VideoSlider.setObjectName("VideoSlider")
        self.horizontalLayout_7.addWidget(self.VideoSlider)
        self.VolumeSlider = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy)
        self.VolumeSlider.setMinimumSize(QtCore.QSize(0, 25))
        self.VolumeSlider.setStyleSheet("QSlider:hover {    \n"
"   background-color: rgb(55, 55, 55);\n"
"}\n"
"QSlider {    \n"
"    background-color: rgb(35,35, 35);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 0, 0);;\n"
"}\n"
"\n"
"")
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setProperty("value", 50)
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.horizontalLayout_7.addWidget(self.VolumeSlider)
        self.verticalLayout_4.addWidget(self.frame)
        self.stackedWidget.addWidget(self.MediaPlayer)
        self.Information = QtWidgets.QWidget()
        self.Information.setObjectName("Information")
        self.label = QtWidgets.QLabel(self.Information)
        self.label.setGeometry(QtCore.QRect(300, 120, 461, 271))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.Information)
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.label_3 = QtWidgets.QLabel(self.Settings)
        self.label_3.setGeometry(QtCore.QRect(180, 140, 731, 261))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.Settings)
        self.horizontalLayout_8.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.verticalLayout_2.addWidget(self.main_body)
        self.main_futer = QtWidgets.QFrame(self.widget)
        self.main_futer.setMinimumSize(QtCore.QSize(25, 20))
        self.main_futer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_futer.setStyleSheet("background-color: #16191d;")
        self.main_futer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_futer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_futer.setObjectName("main_futer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main_futer)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.main_futer)
        self.label_2.setMinimumSize(QtCore.QSize(0, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.main_futer)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "MediaPlayer"))
        self.pushButton_5.setText(_translate("MainWindow", "Settings"))
        self.pushButton_4.setText(_translate("MainWindow", "Information"))
        self.pushButton_3.setText(_translate("MainWindow", "LogOut"))
        self.OpenButton.setText(_translate("MainWindow", "Открыть"))
        self.label.setText(_translate("MainWindow", "Мой индивидуальный проект"))
        self.label_3.setText(_translate("MainWindow", "Скоро здесь будут настройки темы:тёмная и светлая"))
        self.label_2.setText(_translate("MainWindow", "GITHUB: thug-cawa"))
from PySide2.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())