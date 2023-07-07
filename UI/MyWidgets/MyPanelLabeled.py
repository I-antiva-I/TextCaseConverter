from PyQt5 import QtWidgets

from UI.MyWidgets.MyWidgetWithLayout import MyWidgetWithLayout


class MyPanelLabeled(QtWidgets.QGroupBox, MyWidgetWithLayout):
    def __init__(self, name=None, layout=None, label=None):
        super(MyPanelLabeled, self).__init__()

        if name is not None:
            self.setObjectName(name)

        if layout is None:
            self.setLayout(QtWidgets.QVBoxLayout())
        else:
            self.setLayout(layout)

        if label is not None:
            self.setTitle(label)

