import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QMainWindow, QSlider


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton("BUTTON2")
        button2.clicked.connect(self.button2_clicked)

        # widget_layout = QHBoxLayout() #Horizontal
        widget_layout = QVBoxLayout()  # Vertica1
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)

    def button1_clicked(self):
        print("Boton 1 Click")

    def button2_clicked(self):
        print("Boton 2 Click")

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Button Holder app')

        self.button = QPushButton('Press Me!')
        self.setCentralWidget(self.button)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(25)
        self.setCentralWidget(self.slider)
        self.slider.valueChanged.connect(self.respond_slider)

    def button_clicked(self, data):
        print("Boton Click...", data)

    def respond_slider(self, data):
        print("Se ha movido a...", data)


app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

widgetD = RockWidget()
widgetD.show()

app.exec()
