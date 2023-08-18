import pyperclip

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTextEdit, QPushButton

from UI.MyWidgets.MyMainWindow import MyMainWindow


class MainController:
    def __init__(self, mainWindow: MyMainWindow):
        # Control Buttons
        self.buttonPaste:       QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_PASTE")
        self.buttonCopy:        QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_COPY")
        self.buttonClear:       QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_CLEAR")
        # Case Buttons
        self.buttonUpper:       QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_UPPER")
        self.buttonLower:       QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_LOWER")
        self.buttonCapital:     QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_CAPITAL")
        self.buttonSentence:    QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_SENTENCE")
        self.buttonReverse:     QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_REVERSE")
        self.buttonTitle:       QPushButton =      mainWindow.findChild(QtWidgets.QWidget, "BUTTON_TITLE")

        # Text Area
        self.textArea:  QTextEdit =        mainWindow.findChild(QtWidgets.QWidget, "TEXT_AREA")

    # Functions for Control Buttons
    def clearText(self):
        self.textArea.setPlainText("")

    def copyText(self):
        pyperclip.copy(self.textArea.toPlainText())

    def pasteText(self):
        self.textArea.setPlainText(pyperclip.paste())

    # Functions for Case Buttons
    def textToUpper(self):
        string =  self.textArea.toPlainText()
        self.textArea.setPlainText(string.upper())

    def textToLower(self):
        string =  self.textArea.toPlainText()
        self.textArea.setPlainText(string.lower())

    def textToReverse(self):
        string = self.textArea.toPlainText()
        self.textArea.setPlainText(string.swapcase())

    def textToCapitalized(self):
        strings = self.textArea.toPlainText().split(" ")
        capitalized = ""
        for string in strings:
            capitalized += string.capitalize()+" "
        self.textArea.setPlainText(capitalized.strip())

    def textToSentence(self):
        string = self.textArea.toPlainText()
        self.textArea.setPlainText(string.capitalize())

    def textToTitle(self):
        strings = self.textArea.toPlainText().split(" ")
        title = ""
        # Words that should not be capitalized
        exceptions = ["as", "at," "by", "for", "in", "of", "off", "on", "per", "to", "up", "via"]
        for string in strings:
            if string.lower() not in exceptions:
                title += string.capitalize()+" "
            else:
                title += string.lower()+" "
        self.textArea.setPlainText(title.strip())

    # Connect all functions to buttons
    def connectFunctions(self):
        # Control
        self.buttonClear.clicked.connect(lambda: self.clearText())
        self.buttonPaste.clicked.connect(lambda: self.pasteText())
        self.buttonCopy.clicked.connect(lambda:  self.copyText())

        # Case
        self.buttonUpper.clicked.connect(lambda:        self.textToUpper())
        self.buttonLower.clicked.connect(lambda:        self.textToLower())
        self.buttonSentence.clicked.connect(lambda:     self.textToSentence())
        self.buttonReverse.clicked.connect(lambda:      self.textToReverse())
        self.buttonCapital.clicked.connect(lambda:      self.textToCapitalized())
        self.buttonTitle.clicked.connect(lambda:        self.textToTitle())
