from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")
        self.btn_enviar.clicked.connect(self.do_something)

    def do_something(self):
        print(self.txt_nombres.text()," is a ",self.txt_ocupacion.text())


