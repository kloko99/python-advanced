from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
from pathlib import Path


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()

        ui_file = Path(__file__).parent / "design.ui"
        loader = QUiLoader()

        file = QFile(str(ui_file))
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        # Use the loaded UI as the actual content of this dialog
        self.setWindowTitle(self.ui.windowTitle())
        self.resize(self.ui.size())
        self.ui.setParent(self)  # Make sure the loaded UI is a child of the dialog

    def show(self):
        self.ui.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainDialog()
    window.show()
    sys.exit(app.exec())
