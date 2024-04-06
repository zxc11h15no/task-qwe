from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PlayerWindow(object):
    def setupUi(self, PlayerWindow):
        PlayerWindow.setObjectName("PlayerWindow")
        PlayerWindow.resize(400, 550)  # Adjusted the size a little
        self.mainWidget = QtWidgets.QWidget(parent=PlayerWindow)
        self.mainWidget.setObjectName("mainWidget")
        self.listView = QtWidgets.QListWidget(parent=self.mainWidget)  # Renamed to listView
        self.listView.setGeometry(QtCore.QRect(10, 10, 360, 190))  # Adjusted geometry a bit
        self.listView.setObjectName("listView")
        self.layoutWidget = QtWidgets.QWidget(parent=self.mainWidget)  # Renamed to layoutWidget
        self.layoutWidget.setGeometry(QtCore.QRect(20, 210, 340, 280))  # Adjusted geometry a bit
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(parent=self.layoutWidget)  # Renamed to startButton
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(parent=self.layoutWidget)  # Renamed to pauseButton
        self.pauseButton.setObjectName("pauseButton")
        self.verticalLayout.addWidget(self.pauseButton)
        self.updateButton = QtWidgets.QPushButton(parent=self.layoutWidget)  # Renamed to updateButton
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout.addWidget(self.updateButton)
        self.randomButton = QtWidgets.QPushButton(parent=self.layoutWidget)  # Renamed to randomButton
        self.randomButton.setObjectName("randomButton")
        self.verticalLayout.addWidget(self.randomButton)
        PlayerWindow.setCentralWidget(self.mainWidget)
        self.menuBar = QtWidgets.QMenuBar(parent=PlayerWindow)  # Renamed to menuBar
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 24))  # Adjusted the size a bit and renamed
        self.menuBar.setObjectName("menuBar")
        PlayerWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(parent=PlayerWindow)  # Renamed to statusBar
        self.statusBar.setObjectName("statusBar")
        PlayerWindow.setStatusBar(self.statusBar)

        self.retranslateUi(PlayerWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayerWindow)

    def retranslateUi(self, PlayerWindow):
        _translate = QtCore.QCoreApplication.translate
        PlayerWindow.setWindowTitle(_translate("PlayerWindow", "Music Player"))
        self.startButton.setText(_translate("PlayerWindow", "Play"))
        self.pauseButton.setText(_translate("PlayerWindow", "Hold"))
        self.updateButton.setText(_translate("PlayerWindow", "Refresh"))
        self.randomButton.setText(_translate("PlayerWindow", "Shuffle"))