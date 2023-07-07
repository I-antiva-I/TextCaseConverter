from PyQt5 import QtWidgets

from UI.MyWidgets.MyWidgetWithLayout import MyWidgetWithLayout


class MyPanel(QtWidgets.QFrame, MyWidgetWithLayout):
    def __init__(self, name=None, layout=None):
        super(MyPanel, self).__init__()

        if name is not None:
            self.setObjectName(name)

        if layout is None:
            self.setLayout(QtWidgets.QVBoxLayout())
        else:
            self.setLayout(layout)
