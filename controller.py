import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from model import *
from view import *

class Controller:
    def __init__(self):
        self.model = RestClient("http://127.0.0.1:5000")
        self.view = View(self)

    def reset(self):
        self.view.reset()

    def execute(self):
            # Lese den Text aus dem Textfeld
            text = self.view.get_input()
            if len(text) > 0 and text[0].isalpha():
                # Verwende das Model, um die Sprache des Textes zu überprüfen
                reliable, language, short_name, probability = self.model.check_language(text)
                probability = round(probability)
                self.view.update_result(reliable, language, probability)
                self.view.statusbar.showMessage("")
            else:
                self.view.statusbar.showMessage("Die Eingabe ist falsch!")
                # Aktualisiere das Ergebnis-Label mit den Ergebnissen

if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())