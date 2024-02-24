from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import  QMainWindow, QToolBar, QPushButton, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app  # declare an app member
        self.setWindowTitle('Ventana Principal')

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu('&Edit')
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        toolbar = QToolBar('Barra Principal')
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("Alguna Acción", self)
        action1.setStatusTip('Estado de mensaje para alguna accion')
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("homer-simpson.svg"), "Auch", self)
        action2.setStatusTip('Mmm... Rosquillas')
        action2.setCheckable(True)
        action2.triggered.connect(self.toolbar_button_click_homero)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        buttonClick3 = QPushButton("Click here")
        buttonClick3.clicked.connect(self.button3_clicked)
        toolbar.addWidget(buttonClick3)

        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        print('Accion 1 Ejecutada')

    def toolbar_button_click_homero(self, data):
        # print(data and "Ya-hoo" or "Auch")
        self.statusBar().showMessage(data and "Ya-hoo" or "Auch", 1000)

    def button1_clicked(self):
        print("Click en el boton")

    def button3_clicked(self):
        print("Hola aprendices")
