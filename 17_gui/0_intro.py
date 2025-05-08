import sys
from PySide6.QtWidgets import (
    QDialog,
    QApplication,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
)


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        # self.resize(300, 300)  # Größe festlegen
        self.setWindowTitle("Mein erster Dialog")

        self.text = "Hallo, ich bin der Text"
        # Widgets erstellen
        self.label = QLabel(self.text)
        self.btn = QPushButton("Press me!")

        # Aktionen zuweisen
        self.btn.clicked.connect(self.btn_click)

        # Dem Vertikalen Layout zwei Widgets hinzufügen
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(
            self.label,
        )
        self.main_layout.addWidget(self.btn)

        # Layout registrieren
        self.setLayout(self.main_layout)

    def btn_click(self):
        QMessageBox.information(self, "Danke!!!!", "Du hast geklickt!")
        self.label.setText("ich hab geklickt")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec())
