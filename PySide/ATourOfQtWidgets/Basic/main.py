import sys
from PySide6.QtWidgets import QApplication
from PySide.ATourOfQtWidgets.Basic.MainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()