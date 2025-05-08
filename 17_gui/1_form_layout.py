"""
Formular erstellen mit QFormLayout
"""

import sys
from PySide6.QtWidgets import (
    QDialog,
    QApplication,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
    QFormLayout,
    QLineEdit,
)


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        # self.resize(300, 300)  # Größe festlegen
        self.setWindowTitle("Mein erster Dialog")

        # Formularfelder
        self.vorname = QLineEdit()
        self.nachname = QLineEdit()
        self.alter = QLineEdit()
        self.btn = QPushButton("Absenden")

        self.main_layout = QFormLayout()
        self.main_layout.addRow("Vorname:", self.vorname)
        self.main_layout.addRow("Nachname:", self.nachname)
        self.main_layout.addRow("Alter:", self.alter)
        self.main_layout.addRow(self.btn)

        self.setLayout(self.main_layout)

        # Aktion
        self.btn.clicked.connect(self.submit)

    def submit(self):
        """Formular absenden."""
        vorname = self.vorname.text()
        nachname = self.nachname.text()
        alter = self.alter.text()

        print(vorname, nachname, alter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec())
