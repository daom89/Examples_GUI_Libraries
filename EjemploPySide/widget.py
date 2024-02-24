from PySide6.QtWidgets import QWidget
from EjemploPySide.ui_widget import Ui_Widget
from Ejercicio1 import Ejercicio1
from Utils import Utils


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ejercicio 1 - Calcular Cociente")
        self.btn_calcular.clicked.connect(self.calcular_cociente)


    def calcular_cociente(self):
        num_1 = Utils.obtener_entero(self.txt_num_1.text())
        num_2 = Utils.obtener_entero(self.txt_num_2.text())
        obj_ejercicio_1 = Ejercicio1(num_1, num_2)
        self.lbl_resultado.setText(f"El cociente del numero es: {str(obj_ejercicio_1.calcular_cociente().cociente)}")