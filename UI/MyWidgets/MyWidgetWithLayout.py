from PyQt5.QtWidgets import QWidget, QGridLayout


class MyWidgetWithLayout:
    def place(self: QWidget , widget, row=None, col=None, rowSpan=1, colSpan=1):
        # Grid layout
        if type(self.layout()) is QGridLayout:
            if (row is not None) and (col is not None):
                self.layout().addWidget(widget, row, col, rowSpan, colSpan)
            else:
                self.layout().addWidget(widget)
        # VBox/HBox layout
        else:
            self.layout().addWidget(widget)

    def placeAll(self, *widgets):
        for widget in widgets:
            self.place(widget)