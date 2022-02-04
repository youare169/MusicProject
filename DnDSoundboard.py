from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QAction
import pygame, pickle
import time
import os
import tempfile
import ffmpeg, subprocess


class Ui_Soundboard(object):
    def __init__(self):
        self.VoiceClipButtonDict = {}
        self.SoundEffectButtonDict = {}
        self.BackgroundMusicButtonDict = {}
        self.looping = False

    def setupUi(self, Soundboard):
        Soundboard.setObjectName("Soundboard")
        Soundboard.resize(803, 858)
        self.centralwidget = QtWidgets.QWidget(Soundboard)
        self.centralwidget.setObjectName("centralwidget")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(10, 70, 131, 23))
        self.StartButton.setObjectName("StartButton")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(150, 70, 131, 23))
        self.StopButton.setObjectName("StopButton")
        self.BackgroundMusicButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.BackgroundMusicButton_1.setGeometry(QtCore.QRect(10, 100, 131, 61))
        self.BackgroundMusicButton_1.setObjectName("BackgroundMusicButton_1")
        self.BackgroundMusicTitle = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundMusicTitle.setGeometry(QtCore.QRect(20, 30, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.BackgroundMusicTitle.setFont(font)
        self.BackgroundMusicTitle.setObjectName("BackgroundMusicTitle")
        self.BackgroundMusicButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.BackgroundMusicButton_2.setGeometry(QtCore.QRect(150, 100, 131, 61))
        self.BackgroundMusicButton_2.setObjectName("BackgroundMusicButton_2")
        self.BackgroundMusicButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.BackgroundMusicButton_3.setGeometry(QtCore.QRect(290, 100, 131, 61))
        self.BackgroundMusicButton_3.setObjectName("BackgroundMusicButton_3")
        self.VoiceClipTitle = QtWidgets.QLabel(self.centralwidget)
        self.VoiceClipTitle.setGeometry(QtCore.QRect(20, 170, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.VoiceClipTitle.setFont(font)
        self.VoiceClipTitle.setObjectName("VoiceClipTitle")
        self.VoiceClipButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_1.setGeometry(QtCore.QRect(20, 210, 101, 61))
        self.VoiceClipButton_1.setObjectName("VoiceClipButton_1")
        self.BackgroundMusicVolumeSlider_1 = QtWidgets.QSlider(self.centralwidget)
        self.BackgroundMusicVolumeSlider_1.setGeometry(QtCore.QRect(620, 40, 160, 22))
        self.BackgroundMusicVolumeSlider_1.setMaximum(100)
        self.BackgroundMusicVolumeSlider_1.setProperty("value", 100)
        self.BackgroundMusicVolumeSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.BackgroundMusicVolumeSlider_1.setObjectName("BackgroundMusicVolumeSlider_1")
        self.BackgroundVolumeLabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundVolumeLabel_1.setGeometry(QtCore.QRect(470, 40, 141, 21))
        self.BackgroundVolumeLabel_1.setObjectName("BackgroundVolumeLabel_1")
        self.BackgroundMusicVolumeSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.BackgroundMusicVolumeSlider_2.setGeometry(QtCore.QRect(620, 70, 160, 22))
        self.BackgroundMusicVolumeSlider_2.setMaximum(100)
        self.BackgroundMusicVolumeSlider_2.setProperty("value", 100)
        self.BackgroundMusicVolumeSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.BackgroundMusicVolumeSlider_2.setObjectName("BackgroundMusicVolumeSlider_2")
        self.BackgroundVolumeLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundVolumeLabel_2.setGeometry(QtCore.QRect(470, 70, 141, 21))
        self.BackgroundVolumeLabel_2.setObjectName("BackgroundVolumeLabel_2")
        self.BackgroundMusicVolumeSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.BackgroundMusicVolumeSlider_3.setGeometry(QtCore.QRect(620, 100, 160, 22))
        self.BackgroundMusicVolumeSlider_3.setMaximum(100)
        self.BackgroundMusicVolumeSlider_3.setProperty("value", 100)
        self.BackgroundMusicVolumeSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.BackgroundMusicVolumeSlider_3.setObjectName("BackgroundMusicVolumeSlider_3")
        self.BackgroundVolumeLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundVolumeLabel_3.setGeometry(QtCore.QRect(470, 100, 141, 21))
        self.BackgroundVolumeLabel_3.setObjectName("BackgroundVolumeLabel_3")
        self.VoiceClipVolumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.VoiceClipVolumeSlider.setGeometry(QtCore.QRect(620, 130, 160, 22))
        self.VoiceClipVolumeSlider.setMaximum(100)
        self.VoiceClipVolumeSlider.setProperty("value", 100)
        self.VoiceClipVolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VoiceClipVolumeSlider.setObjectName("VoiceClipVolumeSlider")
        self.VoiceClipVolumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.VoiceClipVolumeLabel.setGeometry(QtCore.QRect(470, 130, 141, 21))
        self.VoiceClipVolumeLabel.setObjectName("VoiceClipVolumeLabel")
        self.SoundEffectTitle = QtWidgets.QLabel(self.centralwidget)
        self.SoundEffectTitle.setGeometry(QtCore.QRect(20, 490, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.SoundEffectTitle.setFont(font)
        self.SoundEffectTitle.setObjectName("SoundEffectTitle")
        self.VoiceClipButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_2.setGeometry(QtCore.QRect(130, 210, 101, 61))
        self.VoiceClipButton_2.setObjectName("VoiceClipButton_2")
        self.VoiceClipButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_3.setGeometry(QtCore.QRect(240, 210, 101, 61))
        self.VoiceClipButton_3.setObjectName("VoiceClipButton_3")
        self.VoiceClipButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_4.setGeometry(QtCore.QRect(350, 210, 101, 61))
        self.VoiceClipButton_4.setObjectName("VoiceClipButton_4")
        self.VoiceClipButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_5.setGeometry(QtCore.QRect(460, 210, 101, 61))
        self.VoiceClipButton_5.setObjectName("VoiceClipButton_5")
        self.VoiceClipButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_6.setGeometry(QtCore.QRect(570, 210, 101, 61))
        self.VoiceClipButton_6.setObjectName("VoiceClipButton_6")
        self.VoiceClipButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_7.setGeometry(QtCore.QRect(680, 210, 101, 61))
        self.VoiceClipButton_7.setObjectName("VoiceClipButton_7")
        self.VoiceClipButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_8.setGeometry(QtCore.QRect(20, 280, 101, 61))
        self.VoiceClipButton_8.setObjectName("VoiceClipButton_8")
        self.VoiceClipButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_9.setGeometry(QtCore.QRect(130, 280, 101, 61))
        self.VoiceClipButton_9.setObjectName("VoiceClipButton_9")
        self.VoiceClipButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_10.setGeometry(QtCore.QRect(240, 280, 101, 61))
        self.VoiceClipButton_10.setObjectName("VoiceClipButton_10")
        self.VoiceClipButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_11.setGeometry(QtCore.QRect(350, 280, 101, 61))
        self.VoiceClipButton_11.setObjectName("VoiceClipButton_11")
        self.VoiceClipButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_12.setGeometry(QtCore.QRect(460, 280, 101, 61))
        self.VoiceClipButton_12.setObjectName("VoiceClipButton_12")
        self.VoiceClipButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_13.setGeometry(QtCore.QRect(570, 280, 101, 61))
        self.VoiceClipButton_13.setObjectName("VoiceClipButton_13")
        self.VoiceClipButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_14.setGeometry(QtCore.QRect(680, 280, 101, 61))
        self.VoiceClipButton_14.setObjectName("VoiceClipButton_14")
        self.VoiceClipButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_15.setGeometry(QtCore.QRect(20, 350, 101, 61))
        self.VoiceClipButton_15.setObjectName("VoiceClipButton_15")
        self.VoiceClipButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_16.setGeometry(QtCore.QRect(130, 350, 101, 61))
        self.VoiceClipButton_16.setObjectName("VoiceClipButton_16")
        self.VoiceClipButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_17.setGeometry(QtCore.QRect(240, 350, 101, 61))
        self.VoiceClipButton_17.setObjectName("VoiceClipButton_17")
        self.VoiceClipButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_18.setGeometry(QtCore.QRect(350, 350, 101, 61))
        self.VoiceClipButton_18.setObjectName("VoiceClipButton_18")
        self.VoiceClipButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_19.setGeometry(QtCore.QRect(460, 350, 101, 61))
        self.VoiceClipButton_19.setObjectName("VoiceClipButton_19")
        self.VoiceClipButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_20.setGeometry(QtCore.QRect(570, 350, 101, 61))
        self.VoiceClipButton_20.setObjectName("VoiceClipButton_20")
        self.VoiceClipButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_21.setGeometry(QtCore.QRect(680, 350, 101, 61))
        self.VoiceClipButton_21.setObjectName("VoiceClipButton_21")
        self.VoiceClipButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_22.setGeometry(QtCore.QRect(20, 420, 101, 61))
        self.VoiceClipButton_22.setObjectName("VoiceClipButton_22")
        self.VoiceClipButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_23.setGeometry(QtCore.QRect(130, 420, 101, 61))
        self.VoiceClipButton_23.setObjectName("VoiceClipButton_23")
        self.VoiceClipButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_24.setGeometry(QtCore.QRect(240, 420, 101, 61))
        self.VoiceClipButton_24.setObjectName("VoiceClipButton_24")
        self.VoiceClipButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_25.setGeometry(QtCore.QRect(350, 420, 101, 61))
        self.VoiceClipButton_25.setObjectName("VoiceClipButton_25")
        self.VoiceClipButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_26.setGeometry(QtCore.QRect(460, 420, 101, 61))
        self.VoiceClipButton_26.setObjectName("VoiceClipButton_26")
        self.VoiceClipButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_27.setGeometry(QtCore.QRect(570, 420, 101, 61))
        self.VoiceClipButton_27.setObjectName("VoiceClipButton_27")
        self.VoiceClipButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceClipButton_28.setGeometry(QtCore.QRect(680, 420, 101, 61))
        self.VoiceClipButton_28.setObjectName("VoiceClipButton_28")
        self.SoundEffectButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_1.setGeometry(QtCore.QRect(20, 530, 101, 61))
        self.SoundEffectButton_1.setObjectName("SoundEffectButton_1")
        self.SoundEffectVolumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.SoundEffectVolumeLabel.setGeometry(QtCore.QRect(470, 160, 141, 21))
        self.SoundEffectVolumeLabel.setObjectName("SoundEffectVolumeLabel")
        self.SoundEffectVolumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.SoundEffectVolumeSlider.setGeometry(QtCore.QRect(620, 160, 160, 22))
        self.SoundEffectVolumeSlider.setMaximum(100)
        self.SoundEffectVolumeSlider.setProperty("value", 100)
        self.SoundEffectVolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SoundEffectVolumeSlider.setObjectName("SoundEffectVolumeSlider")
        self.SoundEffectButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_2.setGeometry(QtCore.QRect(130, 530, 101, 61))
        self.SoundEffectButton_2.setObjectName("SoundEffectButton_2")
        self.SoundEffectButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_3.setGeometry(QtCore.QRect(240, 530, 101, 61))
        self.SoundEffectButton_3.setObjectName("SoundEffectButton_3")
        self.SoundEffectButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_4.setGeometry(QtCore.QRect(350, 530, 101, 61))
        self.SoundEffectButton_4.setObjectName("SoundEffectButton_4")
        self.SoundEffectButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_5.setGeometry(QtCore.QRect(460, 530, 101, 61))
        self.SoundEffectButton_5.setObjectName("SoundEffectButton_5")
        self.SoundEffectButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_6.setGeometry(QtCore.QRect(570, 530, 101, 61))
        self.SoundEffectButton_6.setObjectName("SoundEffectButton_6")
        self.SoundEffectButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_7.setGeometry(QtCore.QRect(680, 530, 101, 61))
        self.SoundEffectButton_7.setObjectName("SoundEffectButton_7")
        self.SoundEffectButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_8.setGeometry(QtCore.QRect(20, 600, 101, 61))
        self.SoundEffectButton_8.setObjectName("SoundEffectButton_8")
        self.SoundEffectButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_9.setGeometry(QtCore.QRect(130, 600, 101, 61))
        self.SoundEffectButton_9.setObjectName("SoundEffectButton_9")
        self.SoundEffectButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_10.setGeometry(QtCore.QRect(240, 600, 101, 61))
        self.SoundEffectButton_10.setObjectName("SoundEffectButton_10")
        self.SoundEffectButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_11.setGeometry(QtCore.QRect(350, 600, 101, 61))
        self.SoundEffectButton_11.setObjectName("SoundEffectButton_11")
        self.SoundEffectButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_12.setGeometry(QtCore.QRect(460, 600, 101, 61))
        self.SoundEffectButton_12.setObjectName("SoundEffectButton_12")
        self.SoundEffectButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_13.setGeometry(QtCore.QRect(570, 600, 101, 61))
        self.SoundEffectButton_13.setObjectName("SoundEffectButton_13")
        self.SoundEffectButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_14.setGeometry(QtCore.QRect(680, 600, 101, 61))
        self.SoundEffectButton_14.setObjectName("SoundEffectButton_14")
        self.SoundEffectButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_15.setGeometry(QtCore.QRect(20, 670, 101, 61))
        self.SoundEffectButton_15.setObjectName("SoundEffectButton_15")
        self.SoundEffectButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_16.setGeometry(QtCore.QRect(130, 670, 101, 61))
        self.SoundEffectButton_16.setObjectName("SoundEffectButton_16")
        self.SoundEffectButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_17.setGeometry(QtCore.QRect(240, 670, 101, 61))
        self.SoundEffectButton_17.setObjectName("SoundEffectButton_17")
        self.SoundEffectButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_18.setGeometry(QtCore.QRect(350, 670, 101, 61))
        self.SoundEffectButton_18.setObjectName("SoundEffectButton_18")
        self.SoundEffectButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_19.setGeometry(QtCore.QRect(460, 670, 101, 61))
        self.SoundEffectButton_19.setObjectName("SoundEffectButton_19")
        self.SoundEffectButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_20.setGeometry(QtCore.QRect(570, 670, 101, 61))
        self.SoundEffectButton_20.setObjectName("SoundEffectButton_20")
        self.SoundEffectButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_21.setGeometry(QtCore.QRect(680, 670, 101, 61))
        self.SoundEffectButton_21.setObjectName("SoundEffectButton_21")
        self.SoundEffectButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_22.setGeometry(QtCore.QRect(20, 740, 101, 61))
        self.SoundEffectButton_22.setObjectName("SoundEffectButton_22")
        self.SoundEffectButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_23.setGeometry(QtCore.QRect(130, 740, 101, 61))
        self.SoundEffectButton_23.setObjectName("SoundEffectButton_23")
        self.SoundEffectButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_24.setGeometry(QtCore.QRect(240, 740, 101, 61))
        self.SoundEffectButton_24.setObjectName("SoundEffectButton_24")
        self.SoundEffectButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_25.setGeometry(QtCore.QRect(350, 740, 101, 61))
        self.SoundEffectButton_25.setObjectName("SoundEffectButton_25")
        self.SoundEffectButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_26.setGeometry(QtCore.QRect(460, 740, 101, 61))
        self.SoundEffectButton_26.setObjectName("SoundEffectButton_26")
        self.SoundEffectButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_27.setGeometry(QtCore.QRect(570, 740, 101, 61))
        self.SoundEffectButton_27.setObjectName("SoundEffectButton_27")
        self.SoundEffectButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.SoundEffectButton_28.setGeometry(QtCore.QRect(680, 740, 101, 61))
        self.SoundEffectButton_28.setObjectName("SoundEffectButton_28")
        self.ConfigurationMode = QtWidgets.QCheckBox(self.centralwidget)
        self.ConfigurationMode.setGeometry(QtCore.QRect(240, 0, 131, 21))
        self.ConfigurationMode.setObjectName("ConfigurationMode")
        self.LoadConfiguration = QtWidgets.QPushButton(self.centralwidget)
        self.LoadConfiguration.setGeometry(QtCore.QRect(10, 0, 101, 23))
        self.LoadConfiguration.setObjectName("StartButton_2")
        self.SaveConfiguration = QtWidgets.QPushButton(self.centralwidget)
        self.SaveConfiguration.setGeometry(QtCore.QRect(120, 0, 101, 23))
        self.SaveConfiguration.setObjectName("StartButton_3")
        self.RemoveMode = QtWidgets.QCheckBox(self.centralwidget)
        self.RemoveMode.setGeometry(QtCore.QRect(380, 0, 131, 21))
        self.RemoveMode.setObjectName("RemoveMode")
        Soundboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Soundboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        Soundboard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Soundboard)
        self.statusbar.setObjectName("statusbar")
        Soundboard.setStatusBar(self.statusbar)
        self.actionPick_files = QtWidgets.QAction(Soundboard)
        self.actionPick_files.setObjectName("actionPick_files")
        self.actionMain_window = QtWidgets.QAction(Soundboard)
        self.actionMain_window.setObjectName("actionMain_window")

        self.retranslateUi(Soundboard)
        QtCore.QMetaObject.connectSlotsByName(Soundboard)

    def retranslateUi(self, Soundboard):
        _translate = QtCore.QCoreApplication.translate
        Soundboard.setWindowTitle(_translate("Soundboard", "D&D Soundboard"))
        self.StartButton.setText(_translate("Soundboard", "Start Music"))
        self.StopButton.setText(_translate("Soundboard", "Stop Music"))
        self.BackgroundMusicButton_1.setText(_translate("Soundboard", "lorem ipsum"))
        self.BackgroundMusicTitle.setText(_translate("Soundboard", "Background Music (infinate loops)"))
        self.BackgroundMusicButton_2.setText(_translate("Soundboard", "lorem ipsum"))
        self.BackgroundMusicButton_3.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipTitle.setText(_translate("Soundboard", "Voice Clips"))
        self.VoiceClipButton_1.setText(_translate("Soundboard", "lorem ipsum"))
        self.BackgroundVolumeLabel_1.setText(_translate("Soundboard", "None"))
        self.BackgroundVolumeLabel_2.setText(_translate("Soundboard", "None"))
        self.BackgroundVolumeLabel_3.setText(_translate("Soundboard", "None"))
        self.VoiceClipVolumeLabel.setText(_translate("Soundboard", "Voice clip Volume"))
        self.SoundEffectTitle.setText(_translate("Soundboard", "Sound Effects"))
        self.VoiceClipButton_2.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_3.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_4.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_5.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_6.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_7.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_8.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_9.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_10.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_11.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_12.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_13.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_14.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_15.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_16.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_17.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_18.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_19.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_20.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_21.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_22.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_23.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_24.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_25.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_26.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_27.setText(_translate("Soundboard", "lorem ipsum"))
        self.VoiceClipButton_28.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_1.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectVolumeLabel.setText(_translate("Soundboard", "Sound Effect Volume"))
        self.SoundEffectButton_2.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_3.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_4.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_5.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_6.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_7.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_8.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_9.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_10.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_11.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_12.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_13.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_14.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_15.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_16.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_17.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_18.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_19.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_20.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_21.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_22.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_23.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_24.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_25.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_26.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_27.setText(_translate("Soundboard", "lorem ipsum"))
        self.SoundEffectButton_28.setText(_translate("Soundboard", "lorem ipsum"))
        self.ConfigurationMode.setText(_translate("Soundboard", "Configure soundboard"))
        self.LoadConfiguration.setText(_translate("Soundboard", "Load Configuration"))
        self.SaveConfiguration.setText(_translate("Soundboard", "Save Configuration"))
        self.actionPick_files.setText(_translate("Soundboard", "Pick files"))
        self.actionMain_window.setText(_translate("Soundboard", "Main window"))
        self.RemoveMode.setText(_translate("Soundboard", "Remove sounds"))
        #Custom
        self.startup()

    def startup(self):
        self.VoiceClipButtonDict = {'Button1': make_button_dict(self.VoiceClipButton_1),
                                    'Button2': make_button_dict(self.VoiceClipButton_2),
                                    'Button3': make_button_dict(self.VoiceClipButton_3),
                                    'Button4': make_button_dict(self.VoiceClipButton_4),
                                    'Button5': make_button_dict(self.VoiceClipButton_5),
                                    'Button6': make_button_dict(self.VoiceClipButton_6),
                                    'Button7': make_button_dict(self.VoiceClipButton_7),
                                    'Button8': make_button_dict(self.VoiceClipButton_8),
                                    'Button9': make_button_dict(self.VoiceClipButton_9),
                                    'Button10': make_button_dict(self.VoiceClipButton_10),
                                    'Button11': make_button_dict(self.VoiceClipButton_11),
                                    'Button12': make_button_dict(self.VoiceClipButton_12),
                                    'Button13': make_button_dict(self.VoiceClipButton_13),
                                    'Button14': make_button_dict(self.VoiceClipButton_14),
                                    'Button15': make_button_dict(self.VoiceClipButton_15),
                                    'Button16': make_button_dict(self.VoiceClipButton_16),
                                    'Button17': make_button_dict(self.VoiceClipButton_17),
                                    'Button18': make_button_dict(self.VoiceClipButton_18),
                                    'Button19': make_button_dict(self.VoiceClipButton_19),
                                    'Button20': make_button_dict(self.VoiceClipButton_20),
                                    'Button21': make_button_dict(self.VoiceClipButton_21),
                                    'Button22': make_button_dict(self.VoiceClipButton_22),
                                    'Button23': make_button_dict(self.VoiceClipButton_23),
                                    'Button24': make_button_dict(self.VoiceClipButton_24),
                                    'Button25': make_button_dict(self.VoiceClipButton_25),
                                    'Button26': make_button_dict(self.VoiceClipButton_26),
                                    'Button27': make_button_dict(self.VoiceClipButton_27),
                                    'Button28': make_button_dict(self.VoiceClipButton_28)}

        self.SoundEffectButtonDict = {'Button1': make_button_dict(self.SoundEffectButton_1),
                                      'Button2': make_button_dict(self.SoundEffectButton_2),
                                      'Button3': make_button_dict(self.SoundEffectButton_3),
                                      'Button4': make_button_dict(self.SoundEffectButton_4),
                                      'Button5': make_button_dict(self.SoundEffectButton_5),
                                      'Button6': make_button_dict(self.SoundEffectButton_6),
                                      'Button7': make_button_dict(self.SoundEffectButton_7),
                                      'Button8': make_button_dict(self.SoundEffectButton_8),
                                      'Button9': make_button_dict(self.SoundEffectButton_9),
                                      'Button10': make_button_dict(self.SoundEffectButton_10),
                                      'Button11': make_button_dict(self.SoundEffectButton_11),
                                      'Button12': make_button_dict(self.SoundEffectButton_12),
                                      'Button13': make_button_dict(self.SoundEffectButton_13),
                                      'Button14': make_button_dict(self.SoundEffectButton_14),
                                      'Button15': make_button_dict(self.SoundEffectButton_15),
                                      'Button16': make_button_dict(self.SoundEffectButton_16),
                                      'Button17': make_button_dict(self.SoundEffectButton_17),
                                      'Button18': make_button_dict(self.SoundEffectButton_18),
                                      'Button19': make_button_dict(self.SoundEffectButton_19),
                                      'Button20': make_button_dict(self.SoundEffectButton_20),
                                      'Button21': make_button_dict(self.SoundEffectButton_21),
                                      'Button22': make_button_dict(self.SoundEffectButton_22),
                                      'Button23': make_button_dict(self.SoundEffectButton_23),
                                      'Button24': make_button_dict(self.SoundEffectButton_24),
                                      'Button25': make_button_dict(self.SoundEffectButton_25),
                                      'Button26': make_button_dict(self.SoundEffectButton_26),
                                      'Button27': make_button_dict(self.SoundEffectButton_27),
                                      'Button28': make_button_dict(self.SoundEffectButton_28)}

        self.BackgroundMusicButtonDict = {'Button1': make_button_dict(self.BackgroundMusicButton_1, loop=True, other_label=self.BackgroundVolumeLabel_1),
                                          'Button2': make_button_dict(self.BackgroundMusicButton_2, loop=True, other_label=self.BackgroundVolumeLabel_2),
                                          'Button3': make_button_dict(self.BackgroundMusicButton_3, loop=True, other_label=self.BackgroundVolumeLabel_3)}

        self.SoundEffectButton_1.clicked.connect(self.SoundEffectButton_1_clicked)
        self.SoundEffectButton_2.clicked.connect(self.SoundEffectButton_2_clicked)
        self.SoundEffectButton_3.clicked.connect(self.SoundEffectButton_3_clicked)
        self.SoundEffectButton_4.clicked.connect(self.SoundEffectButton_4_clicked)
        self.SoundEffectButton_5.clicked.connect(self.SoundEffectButton_5_clicked)
        self.SoundEffectButton_6.clicked.connect(self.SoundEffectButton_6_clicked)
        self.SoundEffectButton_7.clicked.connect(self.SoundEffectButton_7_clicked)
        self.SoundEffectButton_8.clicked.connect(self.SoundEffectButton_8_clicked)
        self.SoundEffectButton_9.clicked.connect(self.SoundEffectButton_9_clicked)
        self.SoundEffectButton_10.clicked.connect(self.SoundEffectButton_10_clicked)
        self.SoundEffectButton_11.clicked.connect(self.SoundEffectButton_11_clicked)
        self.SoundEffectButton_12.clicked.connect(self.SoundEffectButton_12_clicked)
        self.SoundEffectButton_13.clicked.connect(self.SoundEffectButton_13_clicked)
        self.SoundEffectButton_14.clicked.connect(self.SoundEffectButton_14_clicked)
        self.SoundEffectButton_15.clicked.connect(self.SoundEffectButton_15_clicked)
        self.SoundEffectButton_16.clicked.connect(self.SoundEffectButton_16_clicked)
        self.SoundEffectButton_17.clicked.connect(self.SoundEffectButton_17_clicked)
        self.SoundEffectButton_18.clicked.connect(self.SoundEffectButton_18_clicked)
        self.SoundEffectButton_19.clicked.connect(self.SoundEffectButton_19_clicked)
        self.SoundEffectButton_20.clicked.connect(self.SoundEffectButton_20_clicked)
        self.SoundEffectButton_21.clicked.connect(self.SoundEffectButton_21_clicked)
        self.SoundEffectButton_22.clicked.connect(self.SoundEffectButton_22_clicked)
        self.SoundEffectButton_23.clicked.connect(self.SoundEffectButton_23_clicked)
        self.SoundEffectButton_24.clicked.connect(self.SoundEffectButton_24_clicked)
        self.SoundEffectButton_25.clicked.connect(self.SoundEffectButton_25_clicked)
        self.SoundEffectButton_26.clicked.connect(self.SoundEffectButton_26_clicked)
        self.SoundEffectButton_27.clicked.connect(self.SoundEffectButton_27_clicked)
        self.SoundEffectButton_28.clicked.connect(self.SoundEffectButton_28_clicked)

        self.VoiceClipButton_1.clicked.connect(self.VoiceClipButton_1_clicked)
        self.VoiceClipButton_2.clicked.connect(self.VoiceClipButton_2_clicked)
        self.VoiceClipButton_3.clicked.connect(self.VoiceClipButton_3_clicked)
        self.VoiceClipButton_4.clicked.connect(self.VoiceClipButton_4_clicked)
        self.VoiceClipButton_5.clicked.connect(self.VoiceClipButton_5_clicked)
        self.VoiceClipButton_6.clicked.connect(self.VoiceClipButton_6_clicked)
        self.VoiceClipButton_7.clicked.connect(self.VoiceClipButton_7_clicked)
        self.VoiceClipButton_8.clicked.connect(self.VoiceClipButton_8_clicked)
        self.VoiceClipButton_9.clicked.connect(self.VoiceClipButton_9_clicked)
        self.VoiceClipButton_10.clicked.connect(self.VoiceClipButton_10_clicked)
        self.VoiceClipButton_11.clicked.connect(self.VoiceClipButton_11_clicked)
        self.VoiceClipButton_12.clicked.connect(self.VoiceClipButton_12_clicked)
        self.VoiceClipButton_13.clicked.connect(self.VoiceClipButton_13_clicked)
        self.VoiceClipButton_14.clicked.connect(self.VoiceClipButton_14_clicked)
        self.VoiceClipButton_15.clicked.connect(self.VoiceClipButton_15_clicked)
        self.VoiceClipButton_16.clicked.connect(self.VoiceClipButton_16_clicked)
        self.VoiceClipButton_17.clicked.connect(self.VoiceClipButton_17_clicked)
        self.VoiceClipButton_18.clicked.connect(self.VoiceClipButton_18_clicked)
        self.VoiceClipButton_19.clicked.connect(self.VoiceClipButton_19_clicked)
        self.VoiceClipButton_20.clicked.connect(self.VoiceClipButton_20_clicked)
        self.VoiceClipButton_21.clicked.connect(self.VoiceClipButton_21_clicked)
        self.VoiceClipButton_22.clicked.connect(self.VoiceClipButton_22_clicked)
        self.VoiceClipButton_23.clicked.connect(self.VoiceClipButton_23_clicked)
        self.VoiceClipButton_24.clicked.connect(self.VoiceClipButton_24_clicked)
        self.VoiceClipButton_25.clicked.connect(self.VoiceClipButton_25_clicked)
        self.VoiceClipButton_26.clicked.connect(self.VoiceClipButton_26_clicked)
        self.VoiceClipButton_27.clicked.connect(self.VoiceClipButton_27_clicked)
        self.VoiceClipButton_28.clicked.connect(self.VoiceClipButton_28_clicked)

        self.BackgroundMusicButton_1.clicked.connect(self.BackgroundMusicButton_1_clicked)
        self.BackgroundMusicButton_2.clicked.connect(self.BackgroundMusicButton_2_clicked)
        self.BackgroundMusicButton_3.clicked.connect(self.BackgroundMusicButton_3_clicked)

        self.StartButton.clicked.connect(self.start_looping)
        self.StopButton.clicked.connect(self.stop_looping)

        self.ConfigurationMode.stateChanged.connect(self.configuration_state_manager)
        self.RemoveMode.stateChanged.connect(self.remove_state_manager)

        self.disable_buttons(self.VoiceClipButtonDict)
        self.disable_buttons(self.SoundEffectButtonDict)
        self.disable_buttons(self.BackgroundMusicButtonDict)

        self.BackgroundMusicVolumeSlider_1.valueChanged.connect(self.change_background1_volume)
        self.BackgroundMusicVolumeSlider_2.valueChanged.connect(self.change_background2_volume)
        self.BackgroundMusicVolumeSlider_3.valueChanged.connect(self.change_background3_volume)
        self.VoiceClipVolumeSlider.valueChanged.connect(self.change_clip_volume)
        self.SoundEffectVolumeSlider.valueChanged.connect(self.change_effect_volume)

        self.SaveConfiguration.clicked.connect(self.save_configuration)
        self.LoadConfiguration.clicked.connect(self.load_configuration)

        pygame.mixer.init()
        pygame.init()
        pygame.mixer.set_num_channels(26)

    def close_event(self):
        # close out the open temp files
        pass

    def remove_state_manager(self):
        if self.RemoveMode.isChecked() and not self.ConfigurationMode.isChecked():
            self.StartButton.setEnabled(False)
            self.StopButton.setEnabled(False)
            self.stop_looping()
            enable_buttons(self.VoiceClipButtonDict)
            enable_buttons(self.SoundEffectButtonDict)
            enable_buttons(self.BackgroundMusicButtonDict)

        else:
            self.StartButton.setEnabled(True)
            self.StopButton.setEnabled(True)
            self.disable_buttons(self.VoiceClipButtonDict)
            self.disable_buttons(self.SoundEffectButtonDict)
            self.disable_buttons(self.BackgroundMusicButtonDict)

        self.refresh_buttons(self.BackgroundMusicButtonDict)
        self.refresh_buttons(self.VoiceClipButtonDict)
        self.refresh_buttons(self.SoundEffectButtonDict)

    def save_configuration(self):
        file_info = QFileDialog.getSaveFileName(caption='Save configuration', filter='Soundboard Files (*DnDSB)')[0]
        to_save = {'Background': self.clear_unsavable(self.BackgroundMusicButtonDict),
                   'SoundEffect': self.clear_unsavable(self.SoundEffectButtonDict),
                   'VoiceClip': self.clear_unsavable(self.VoiceClipButtonDict)}

        with open(file_info + '.DnDSB', 'wb') as handle:
            pickle.dump(to_save, handle)

    def clear_unsavable(self, button_dict):
        out = []
        for button in button_dict.keys():
            out.append({'file': button_dict[button]['file'], 'button': button})
        return out

    def load_configuration(self):
        file_info = QFileDialog.getOpenFileName(caption='Select file', filter="SoundboardFiles (*DnDSB)")[0]
        print(file_info)
        with open(file_info, 'rb') as handle:
            b = pickle.load(handle)

        for file_dict in b['Background']:
            self.BackgroundMusicButtonDict[file_dict['button']]['file'] = file_dict['file']
        for file_dict in b['VoiceClip']:
            self.VoiceClipButtonDict[file_dict['button']]['file'] = file_dict['file']
        for file_dict in b['SoundEffect']:
            self.SoundEffectButtonDict[file_dict['button']]['file'] = file_dict['file']

        self.refresh_buttons(self.BackgroundMusicButtonDict)
        self.refresh_buttons(self.VoiceClipButtonDict)
        self.refresh_buttons(self.SoundEffectButtonDict)
        self.ConfigurationMode.setChecked(True)
        self.ConfigurationMode.setChecked(False)

    def refresh_buttons(self, button_dict):
        for button in button_dict.values():
            if button['file'] is not None:
                self.add_sound(button['file'], button)

    def change_background1_volume(self):
        volume = self.BackgroundMusicVolumeSlider_1.value() / 100
        self.BackgroundMusicButtonDict['Button1']['sound'].set_volume(volume)
        self.BackgroundMusicButtonDict['Button1']['volume'] = volume

    def change_background2_volume(self):
        volume = self.BackgroundMusicVolumeSlider_2.value() / 100
        self.BackgroundMusicButtonDict['Button2']['sound'].set_volume(volume)
        self.BackgroundMusicButtonDict['Button2']['volume'] = volume

    def change_background3_volume(self):
        volume = self.BackgroundMusicVolumeSlider_3.value() / 100
        self.BackgroundMusicButtonDict['Button3']['sound'].set_volume(volume)
        self.BackgroundMusicButtonDict['Button3']['volume'] = volume

    def change_clip_volume(self):
        self.change_dict_volume(self.VoiceClipButtonDict, volume=self.VoiceClipVolumeSlider.value()/100)

    def change_effect_volume(self):
        self.change_dict_volume(self.SoundEffectButtonDict, volume=self.SoundEffectVolumeSlider.value()/100)

    def change_dict_volume(self, button_dict, volume):
        for button in button_dict.values():
            if button['sound'] is not None:
                button['sound'].set_volume(volume)

    def configuration_state_manager(self):
        if self.ConfigurationMode.isChecked() and not self.RemoveMode.isChecked():
            self.StartButton.setEnabled(False)
            self.StopButton.setEnabled(False)
            self.stop_looping()
            enable_buttons(self.VoiceClipButtonDict)
            enable_buttons(self.SoundEffectButtonDict)
            enable_buttons(self.BackgroundMusicButtonDict)

        else:
            self.StartButton.setEnabled(True)
            self.StopButton.setEnabled(True)
            self.disable_buttons(self.VoiceClipButtonDict)
            self.disable_buttons(self.SoundEffectButtonDict)
            self.disable_buttons(self.BackgroundMusicButtonDict)

        self.refresh_buttons(self.BackgroundMusicButtonDict)
        self.refresh_buttons(self.VoiceClipButtonDict)
        self.refresh_buttons(self.SoundEffectButtonDict)

    def button_manager(self, button, kill_sound1=None, kill_sound2=None):
        if self.ConfigurationMode.isChecked():
            self.select_file(button)
        elif self.RemoveMode.isChecked():
            self.clear_button(button)
        else:
            if button['loop']:
                self.play_loop(button, kill_sound1, kill_sound2)
            else:
                self.play_momentary(button['sound'])

    def clear_button(self, button):
        button['file'] = None
        button['sound'] = None
        button['playing'] = False
        button['instance'].setText('None')
        button['instance'].setEnabled(False)
        if button['other_label'] is not None:
            button['other_label'].setText('None')

    def select_file(self, button):
        file_info = QFileDialog.getOpenFileName(caption='Select file', filter="Sound Files (*.wav)")[0]
        if file_info.upper().endswith('.WAV'):
            self.add_sound(sound_path=file_info, button=button)
        #elif file_info.upper().endswith('.MP3'):
            #self.add_mp3(sound_path=file_info, button=button)

    def add_mp3(self, sound_path, button):
        # create a wav copy in a temp file, and store the temp file in the array
        new_sound_path = sound_path.split('.')[0] + ".wav"
        subprocess.call(['ffmpeg', '-i', sound_path, new_sound_path])
        self.add_sound(sound_path=new_sound_path, button=button)

    def add_sound(self, sound_path, button):
        button['sound'] = pygame.mixer.Sound(sound_path)
        button['file'] = sound_path
        file_name = os.path.basename(sound_path).split('.')[0]
        button['instance'].setText(file_name.replace(' ', '\n').replace('_', '\n'))
        if button['other_label'] is not None:
            button['other_label'].setText(file_name)

    def play_momentary(self, sound):
        if sound is not None:
            sound.play()

    def start_looping(self):
        self.looping = True
        for button in self.BackgroundMusicButtonDict.values():
            if button['sound'] is not None:
                button['sound'].play(loops=-1, fade_ms=500)
                button['sound'].set_volume(0)
                button['instance'].setEnabled(True)

    def stop_looping(self):
        self.looping = False
        for button in self.BackgroundMusicButtonDict.values():
            if button['sound'] is not None:
                button['sound'].stop()
                button['instance'].setEnabled(False)

    def play_loop(self, sound, kill_sound1, kill_sound2):
        ramp_value = 0
        ramp_step = 0.1
        while ramp_value < sound['volume']:
            ramp_value += ramp_step

            sound['sound'].set_volume(ramp_value)
            if kill_sound1['sound'] is not None:
                kill_sound1['sound'].set_volume(sound['volume']-ramp_value)
            if kill_sound2['sound'] is not None:
                kill_sound2['sound'].set_volume(sound['volume']-ramp_value)
            time.sleep(0.0005)
        kill_sound1['sound'].set_volume(0)
        kill_sound2['sound'].set_volume(0)
        sound['playing'] = True
        kill_sound1['playing'] = False
        kill_sound2['playing'] = False
    """
    This shit is why we don't make GUI applications in python. Since the button clicked event doesn't
    give the function access to the button object, it is not possible to make a generic function which
    changes behavior based on the button which invoked it. It's stupid. So this horrible bull shit does
    what the backend should have done to start with. 50/50 chance this feature actually exists, and I
    just couldn't find it.
    """

    def SoundEffectButton_1_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button1'])

    def SoundEffectButton_2_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button2'])

    def SoundEffectButton_3_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button3'])

    def SoundEffectButton_4_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button4'])

    def SoundEffectButton_5_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button5'])

    def SoundEffectButton_6_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button6'])

    def SoundEffectButton_7_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button7'])

    def SoundEffectButton_8_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button8'])

    def SoundEffectButton_9_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button9'])

    def SoundEffectButton_10_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button10'])

    def SoundEffectButton_11_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button11'])

    def SoundEffectButton_12_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button12'])

    def SoundEffectButton_13_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button13'])

    def SoundEffectButton_14_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button14'])

    def SoundEffectButton_15_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button15'])

    def SoundEffectButton_16_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button16'])

    def SoundEffectButton_17_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button17'])

    def SoundEffectButton_18_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button18'])

    def SoundEffectButton_19_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button19'])

    def SoundEffectButton_20_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button20'])

    def SoundEffectButton_21_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button21'])

    def SoundEffectButton_22_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button22'])

    def SoundEffectButton_23_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button23'])

    def SoundEffectButton_24_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button24'])

    def SoundEffectButton_25_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button25'])

    def SoundEffectButton_26_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button26'])

    def SoundEffectButton_27_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button27'])

    def SoundEffectButton_28_clicked(self):
        self.button_manager(self.SoundEffectButtonDict['Button28'])

    def VoiceClipButton_1_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button1'])

    def VoiceClipButton_2_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button2'])

    def VoiceClipButton_3_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button3'])

    def VoiceClipButton_4_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button4'])

    def VoiceClipButton_5_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button5'])

    def VoiceClipButton_6_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button6'])

    def VoiceClipButton_7_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button7'])

    def VoiceClipButton_8_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button8'])

    def VoiceClipButton_9_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button9'])

    def VoiceClipButton_10_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button10'])

    def VoiceClipButton_11_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button11'])

    def VoiceClipButton_12_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button12'])

    def VoiceClipButton_13_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button13'])

    def VoiceClipButton_14_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button14'])

    def VoiceClipButton_15_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button15'])

    def VoiceClipButton_16_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button16'])

    def VoiceClipButton_17_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button17'])

    def VoiceClipButton_18_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button18'])

    def VoiceClipButton_19_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button19'])

    def VoiceClipButton_20_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button20'])

    def VoiceClipButton_21_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button21'])

    def VoiceClipButton_22_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button22'])

    def VoiceClipButton_23_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button23'])

    def VoiceClipButton_24_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button24'])

    def VoiceClipButton_25_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button25'])

    def VoiceClipButton_26_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button26'])

    def VoiceClipButton_27_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button27'])

    def VoiceClipButton_28_clicked(self):
        self.button_manager(self.VoiceClipButtonDict['Button28'])

    def BackgroundMusicButton_1_clicked(self):
        self.button_manager(self.BackgroundMusicButtonDict['Button1'], self.BackgroundMusicButtonDict['Button2'], self.BackgroundMusicButtonDict['Button3'])

    def BackgroundMusicButton_2_clicked(self):
        self.button_manager(self.BackgroundMusicButtonDict['Button2'], self.BackgroundMusicButtonDict['Button1'], self.BackgroundMusicButtonDict['Button3'])

    def BackgroundMusicButton_3_clicked(self):
        self.button_manager(self.BackgroundMusicButtonDict['Button3'], self.BackgroundMusicButtonDict['Button1'], self.BackgroundMusicButtonDict['Button2'])

    """
    End the horrible bull shit
    """

    def disable_buttons(self, button_dict):
        for button in button_dict.values():
            if button['sound'] is None:
                button['instance'].setText('None')
                button['instance'].setEnabled(False)
            elif button['loop'] and not self.looping:
                button['instance'].setEnabled(False)


def enable_buttons(button_dict):
    for button in button_dict.values():
        button['instance'].setEnabled(True)
        if button['sound'] is None:
            button['instance'].setText('Select File')


def make_button_dict(button, loop=False, other_label=None, temp_file=None):
    return {'instance': button, 'file': None, 'sound': None, 'loop': loop, 'other_label': other_label, 'volume': 1, 'playing': False, 'temp_file': temp_file}


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Soundboard = QtWidgets.QMainWindow()
    ui = Ui_Soundboard()
    app.lastWindowClosed.connect(ui.close_event)
    ui.setupUi(Soundboard)
    Soundboard.show()
    sys.exit(app.exec_())
