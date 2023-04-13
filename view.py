from PyQt6.QtWidgets import *
from PyQt6 import uic

import controller

class View(QMainWindow):
    input: QLineEdit
    result: QLabel
    pb_close: QPushButton
    pb_reset: QPushButton
    pb_check: QPushButton
    statusbar: QStatusBar

    def __init__(self, c: controller.Controller):
        super().__init__()
        uic.loadUi("CLDS.ui", self)
        self.pb_reset.clicked.connect(c.reset)
        self.pb_check.clicked.connect(c.execute)

    def reset(self) -> None:
        self.input.setText("")
        self.result.setText("")
        self.statusbar.showMessage("")

    def update_result(self, reliable, language,probability):
        if reliable:
            text = "Reliable: " + "<b>Yes</b>"
        else:
            text = "Reliable: " + "<b>No</b>"
        text += "<br>Language: " + "<b>" + str(language) + "</b>"
        text += "<br>Probability: " + "<b>" + str(probability) + "%" + "</b>"
        self.result.setText(text)

    def get_input(self) -> str:
        return self.input.text()
