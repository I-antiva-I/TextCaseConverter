from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor


class MyPushButton(QtWidgets.QPushButton):
    def __init__(self, name=None, text=None):
        super(MyPushButton, self).__init__()

        if name is not None:
            self.setObjectName(name)

        if text is None:
            self.setText("My Button")
        else:
            self.setText(text)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setXOffset(4)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QColor("#343434"))
        self.setGraphicsEffect(self.shadow)

    def enterEvent(self, QEvent):
        super().leaveEvent(QEvent)
        self.shadow.setColor(QColor("#4169D1"))

    def leaveEvent(self, QEvent):
        super().leaveEvent(QEvent)
        self.shadow.setColor(QColor("#343434"))

    def mousePressEvent(self, QEvent):
        super().mousePressEvent(QEvent)
        self.shadow.setColor(QColor("#DCDCDC"))

    def mouseReleaseEvent(self, QEvent):
        super().mouseReleaseEvent(QEvent)
        self.shadow.setColor(QColor("#4169D1"))

