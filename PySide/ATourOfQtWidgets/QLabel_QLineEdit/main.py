from PySide6.QtWidgets import QApplication
from PySide.ATourOfQtWidgets.QLabel_QLineEdit.widget import Widget
import sys

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()