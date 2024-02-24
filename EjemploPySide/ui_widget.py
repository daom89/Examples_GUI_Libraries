from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(248, 135)
        self.btn_calcular = QPushButton(Widget)
        self.btn_calcular.setObjectName(u"btn_calcular")
        self.btn_calcular.setGeometry(QRect(80, 70, 75, 24))
        self.lbl_resultado = QLabel(Widget)
        self.lbl_resultado.setObjectName(u"lbl_resultado")
        self.lbl_resultado.setGeometry(QRect(20, 100, 191, 16))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 41, 58, 16))
        self.txt_num_2 = QLineEdit(Widget)
        self.txt_num_2.setObjectName(u"txt_num_2")
        self.txt_num_2.setGeometry(QRect(90, 40, 133, 22))
        self.txt_num_1 = QLineEdit(Widget)
        self.txt_num_1.setObjectName(u"txt_num_1")
        self.txt_num_1.setGeometry(QRect(90, 10, 133, 22))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 11, 61, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.btn_calcular.setText(QCoreApplication.translate("Widget", u"Calcular", None))
        self.lbl_resultado.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"Numero 2", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Numero 1", None))
    # retranslateUi

