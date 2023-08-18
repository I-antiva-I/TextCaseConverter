import json

from PyQt5 import QtWidgets, QtGui

from UI.MyWidgets.MyPanel import MyPanel
from UI.MyWidgets.MyPanelLabeled import MyPanelLabeled
from UI.MyWidgets.MyPushButton import MyPushButton


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # The super function in Python takes two optional parameters:
        # 1st -  name of the subclass
        # 2nd -  object of the subclass
        super(MyMainWindow, self).__init__()

        # Main Window properties
        self.setObjectName("MAIN_WINDOW")
        self.setWindowTitle("Text Case Converter")
        self.setWindowIcon(QtGui.QIcon("UI/IMGs/Icon_Main.svg"))
        self.resize(500, 500)

        # Main Panel
        # It's Best Practice to use a Central Widget in Main Window
        # https://doc.qt.io/qt-5/qmainwindow.html#details
        self.mainPanel = MyPanel()
        self.setCentralWidget(self.mainPanel)

        self.prepare()
        self.applyCSS()

    def applyCSS(self):
        pathToCSS =     "UI/CSS/styles.css"
        pathToVars =    "UI/CSS/variables.json"

        stringCSS = open(pathToCSS, "r").read()
        dataVars: dict =  json.load(open(pathToVars))

        for key, value in dataVars.items():
            stringCSS = stringCSS.replace(key, value)

        self.setStyleSheet(stringCSS)

    def prepare(self):
        # Panel for Case Buttons
        panelCaseButtons = MyPanelLabeled(label="Case Transformations", layout=QtWidgets.QGridLayout())
        panelCaseButtons.layout().setSpacing(12)
        # Text Case Buttons
        buttonCaseUpper =           MyPushButton(text="Upper",          name="BUTTON_UPPER")
        buttonCaseLower =           MyPushButton(text="Lower",          name="BUTTON_LOWER")
        buttonCaseCapital =         MyPushButton(text="Capitalized",    name="BUTTON_CAPITAL")
        buttonCaseSentence =        MyPushButton(text="Sentence",       name="BUTTON_SENTENCE")
        buttonCaseReverse =         MyPushButton(text="Reverse",        name="BUTTON_REVERSE")
        buttonCaseTitle =           MyPushButton(text="Title",          name="BUTTON_TITLE")
        # Placement of Case Buttons
        panelCaseButtons.place(buttonCaseUpper,         0, 0)
        panelCaseButtons.place(buttonCaseLower,         1, 0)
        panelCaseButtons.place(buttonCaseCapital,       0, 2)
        panelCaseButtons.place(buttonCaseSentence,      0, 1)
        panelCaseButtons.place(buttonCaseReverse,       1, 1)
        panelCaseButtons.place(buttonCaseTitle,         1, 2)

        # Panel for Control Buttons
        panelTextButtons = MyPanelLabeled(label="Controls", layout=QtWidgets.QHBoxLayout())
        panelTextButtons.layout().setSpacing(12)
        # Control Buttons
        buttonTextClear =   MyPushButton(text="Clear",          name="BUTTON_CLEAR")
        buttonTextPaste =   MyPushButton(text="Paste",          name="BUTTON_PASTE")
        buttonTextCopy =    MyPushButton(text="Copy",           name="BUTTON_COPY")
        # Placement of Control Buttons
        panelTextButtons.placeAll(buttonTextClear, buttonTextPaste, buttonTextCopy)

        # Panel for Text Area
        panelTextArea = MyPanelLabeled(label="Text")
        # Text Area
        textArea = QtWidgets.QTextEdit()
        textArea.setObjectName("TEXT_AREA")
        # Placement of Text Area
        panelTextArea.place(textArea)

        # Placement of Panels
        self.mainPanel.placeAll(panelCaseButtons, panelTextButtons, panelTextArea)
