from PySide6.QtWidgets import QApplication, QDialog
from mydesign import Ui_Dialog  # aus der kompilierten Datei
import qdarkstyle


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # initialisiert die UI in diesem Dialog

        self.setWindowTitle("Mein Dialog")
        self.ui.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button wurde geklickt")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = MainDialog()
    window.show()
    sys.exit(app.exec())
