from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pygame
import time
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_BestMusicThing(object):
    def setupUi(self, BestMusicThing):
        BestMusicThing.setObjectName("BestMusicThing")
        BestMusicThing.resize(672, 650)
        self.centralwidget = QtWidgets.QWidget(BestMusicThing)
        self.centralwidget.setObjectName("centralwidget")
        self.PlebMusicPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlebMusicPathButton.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.PlebMusicPathButton.setObjectName("PlebMusicPathButton")
        self.ChadMusicPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChadMusicPathButton.setGeometry(QtCore.QRect(10, 40, 111, 23))
        self.ChadMusicPathButton.setObjectName("ChadMusicPathButton")
        self.StartMusicButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartMusicButton.setGeometry(QtCore.QRect(20, 480, 101, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.StartMusicButton.setPalette(palette)
        self.StartMusicButton.setObjectName("StartMusicButton")
        self.StopMusicButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopMusicButton.setGeometry(QtCore.QRect(20, 540, 101, 51))
        self.StopMusicButton.setObjectName("StopMusicButton")
        self.MakeChadLoudButton = QtWidgets.QPushButton(self.centralwidget)
        self.MakeChadLoudButton.setGeometry(QtCore.QRect(470, 410, 191, 91))
        self.MakeChadLoudButton.setObjectName("MakeChadLoudButton")
        self.MakePlebLoudButton = QtWidgets.QPushButton(self.centralwidget)
        self.MakePlebLoudButton.setGeometry(QtCore.QRect(470, 510, 191, 91))
        self.MakePlebLoudButton.setObjectName("MakePlebLoudButton")
        self.PlebMusicPath = QtWidgets.QLabel(self.centralwidget)
        self.PlebMusicPath.setGeometry(QtCore.QRect(130, 10, 531, 20))
        self.PlebMusicPath.setObjectName("PlebMusicPath")
        self.ChadMusicPath = QtWidgets.QLabel(self.centralwidget)
        self.ChadMusicPath.setGeometry(QtCore.QRect(130, 40, 531, 20))
        self.ChadMusicPath.setObjectName("ChadMusicPath")
        self.TransMusicPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.TransMusicPathButton.setGeometry(QtCore.QRect(10, 70, 111, 23))
        self.TransMusicPathButton.setObjectName("TransMusicPathButton")
        self.TransMusicPath = QtWidgets.QLabel(self.centralwidget)
        self.TransMusicPath.setGeometry(QtCore.QRect(130, 70, 531, 20))
        self.TransMusicPath.setObjectName("TransMusicPath")
        self.NonCombatMusicPath = QtWidgets.QLabel(self.centralwidget)
        self.NonCombatMusicPath.setGeometry(QtCore.QRect(130, 100, 531, 20))
        self.NonCombatMusicPath.setObjectName("NonCombatMusicPath")
        self.NonCombatMusicPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.NonCombatMusicPathButton.setGeometry(QtCore.QRect(10, 100, 111, 23))
        self.NonCombatMusicPathButton.setObjectName("NonCombatMusicPathButton")
        self.MakeNonCombatLoudButton = QtWidgets.QPushButton(self.centralwidget)
        self.MakeNonCombatLoudButton.setGeometry(QtCore.QRect(470, 310, 191, 91))
        self.MakeNonCombatLoudButton.setObjectName("MakeNonCombatLoudButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 150, 381, 271))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        BestMusicThing.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BestMusicThing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        BestMusicThing.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(BestMusicThing)
        self.statusBar.setObjectName("statusBar")
        BestMusicThing.setStatusBar(self.statusBar)

        self.retranslateUi(BestMusicThing)
        QtCore.QMetaObject.connectSlotsByName(BestMusicThing)


        # My custom shit
        self.onPetersComputer = False
        self.rampStep = 0.1
        self.playing = False

        self.PlebMusicPathButton.clicked.connect(self.getPlebFile)
        self.ChadMusicPathButton.clicked.connect(self.getChadFile)
        self.StartMusicButton.clicked.connect(self.startMusic)
        self.StopMusicButton.clicked.connect(self.stopMusic)
        self.MakeChadLoudButton.clicked.connect(self.switchToChad)
        self.MakePlebLoudButton.clicked.connect(self.switchToPleb)
        self.MakeNonCombatLoudButton.clicked.connect(self.switchToNonCombat)
        self.TransMusicPathButton.clicked.connect(self.getTransitionFile)
        self.NonCombatMusicPathButton.clicked.connect(self.getNoCombatFile)
        pygame.mixer.init()
        pygame.init()

        pygame.mixer.set_num_channels(26)
        self.PlebSound = None
        self.ChadSound = None
        self.TransSound = None
        self.NonCombatSound = None
        self.nonCombatTransSound = pygame.mixer.Sound(resource_path('Victory Sound Effect.wav'))
        self.movie = QtGui.QMovie(resource_path('NonCombat.gif'))

        self.chadVolume = 0
        self.plebVolume = 0
        self.nonCombatVolume = 1


    def retranslateUi(self, BestMusicThing):
        _translate = QtCore.QCoreApplication.translate
        BestMusicThing.setWindowTitle(_translate("BestMusicThing", "BestMusicThing"))
        self.PlebMusicPathButton.setText(_translate("BestMusicThing", "Pleb Music File"))
        self.ChadMusicPathButton.setText(_translate("BestMusicThing", "Big Chad Music File"))
        self.StartMusicButton.setText(_translate("BestMusicThing", "Start Music"))
        self.StopMusicButton.setText(_translate("BestMusicThing", "Stop Music"))
        self.MakeChadLoudButton.setText(_translate("BestMusicThing", "Switch to Big Chad Music"))
        self.MakePlebLoudButton.setText(_translate("BestMusicThing", "Switch to Pleb Music"))
        self.PlebMusicPath.setText(_translate("BestMusicThing", "TextLabel"))
        self.ChadMusicPath.setText(_translate("BestMusicThing", "TextLabel"))
        self.TransMusicPathButton.setText(_translate("BestMusicThing", "Combat Transition File"))
        self.TransMusicPath.setText(_translate("BestMusicThing", "TextLabel"))
        self.NonCombatMusicPath.setText(_translate("BestMusicThing", "TextLabel"))
        self.NonCombatMusicPathButton.setText(_translate("BestMusicThing", "Non-Combat Music"))
        self.MakeNonCombatLoudButton.setText(_translate("BestMusicThing", "Switch to non-combat music"))
        self.label.setText(_translate("BestMusicThing", ""))

    def getPlebFile(self):
        self.PlebMusicPath.setText(QFileDialog.getOpenFileName(caption='select pleb music')[0])

    def getChadFile(self):
        self.ChadMusicPath.setText(QFileDialog.getOpenFileName(caption='select chad music')[0])

    def getTransitionFile(self):
        self.TransMusicPath.setText(QFileDialog.getOpenFileName(caption='select transition music')[0])

    def getNoCombatFile(self):
        self.NonCombatMusicPath.setText(QFileDialog.getOpenFileName(caption='select non-combat music')[0])

    def startMusic(self):
        self.playing = True
        if self.PlebMusicPath.text() != 'TextLabel' and self.ChadMusicPath.text() != 'TextLabel' and self.NonCombatMusicPath.text() != 'TextLabel':
            if self.ChadSound is not None:
                self.ChadSound.stop()
            if self.PlebSound is not None:
                self.PlebSound.stop()
            self.label.setMovie(self.movie)
            self.movie.start()
            self.PlebSound = pygame.mixer.Sound(self.PlebMusicPath.text())
            self.ChadSound = pygame.mixer.Sound(self.ChadMusicPath.text())
            self.TransSound = pygame.mixer.Sound(self.TransMusicPath.text())
            self.NonCombatSound = pygame.mixer.Sound(self.NonCombatMusicPath.text())
            self.PlebSound.play(loops=-1, fade_ms=500)
            self.ChadSound.play(loops=-1, fade_ms=500)
            self.NonCombatSound.play(loops=-1, fade_ms=500)
            self.PlebSound.set_volume(self.plebVolume)
            self.ChadSound.set_volume(self.chadVolume)
            self.NonCombatSound.set_volume(self.nonCombatVolume)

    def stopMusic(self):
        self.playing = False
        self.label.clear()
        if self.ChadSound is not None:
            self.ChadSound.stop()
            self.ChadSound = None

        if self.PlebSound is not None:
            self.PlebSound.stop()
            self.PlebSound = None

        if self.NonCombatSound is not None:
            self.NonCombatSound.stop()
            self.NonCombatSound = None

        if self.TransSound is not None:
            self.TransSound.stop()
            self.TransSound = None

    def switchToChad(self):
        if self.PlebSound is not None and self.ChadSound is not None and self.NonCombatSound is not None:
            self.TransSound.play()

            self.movie = QtGui.QMovie(resource_path('Chad.gif'))
            self.label.setMovie(self.movie)
            self.movie.start()
            while self.chadVolume < 1 or self.plebVolume > 0 or self.nonCombatVolume > 0:
                self.nonCombatVolume -= self.rampStep
                self.plebVolume -= self.rampStep
                self.chadVolume += self.rampStep

                if self.plebVolume < 0:
                    self.plebVolume = 0
                if self.nonCombatVolume < 0:
                    self.nonCombatVolume = 0
                if self.chadVolume > 1:
                    self.chadVolume = 1

                self.PlebSound.set_volume(self.plebVolume)
                self.ChadSound.set_volume(self.chadVolume)
                self.NonCombatSound.set_volume(self.nonCombatVolume)
                time.sleep(0.0005)

    def switchToPleb(self):
        if self.PlebSound is not None and self.ChadSound is not None and self.NonCombatSound is not None:
            self.TransSound.play()
            self.movie = QtGui.QMovie(resource_path('Pleb.gif'))
            self.label.setMovie(self.movie)
            self.movie.start()
            while self.plebVolume < 1 or self.chadVolume > 0 or self.nonCombatVolume > 0:
                self.chadVolume -= self.rampStep
                self.nonCombatVolume -= self.rampStep
                self.plebVolume += self.rampStep

                if self.chadVolume < 0:
                    self.chadVolume = 0
                if self.nonCombatVolume < 0:
                    self.nonCombatVolume = 0
                if self.plebVolume > 1:
                    self.plebVolume = 1

                self.PlebSound.set_volume(self.plebVolume)
                self.ChadSound.set_volume(self.chadVolume)
                self.NonCombatSound.set_volume(self.nonCombatVolume)
                time.sleep(0.0005)

    def switchToNonCombat(self):
        if self.PlebSound is not None and self.ChadSound is not None and self.NonCombatSound is not None:
            self.nonCombatTransSound.play()
            self.movie = QtGui.QMovie(resource_path('NonCombat.gif'))
            self.label.setMovie(self.movie)
            self.movie.start()
            while self.nonCombatVolume < 1 or self.chadVolume > 0 or self.plebVolume > 0:
                self.chadVolume -= self.rampStep
                self.plebVolume -= self.rampStep
                self.nonCombatVolume += self.rampStep

                if self.chadVolume < 0:
                    self.chadVolume = 0
                if self.plebVolume < 0:
                    self.plebVolume = 0
                if self.nonCombatVolume > 1:
                    self.nonCombatVolume = 1

                self.PlebSound.set_volume(self.plebVolume)
                self.ChadSound.set_volume(self.chadVolume)
                self.NonCombatSound.set_volume(self.nonCombatVolume)
                time.sleep(0.0005)

    def infectPetersComputerWithVirus(self):
        # Shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        if self.onPetersComputer:
            deploy_aids = True
            much_sneak = True
            do_crime = True
            tell_nobody = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BestMusicThing = QtWidgets.QMainWindow()
    ui = Ui_BestMusicThing()
    ui.setupUi(BestMusicThing)
    BestMusicThing.show()
    sys.exit(app.exec_())
