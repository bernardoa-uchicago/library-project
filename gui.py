import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

app = QApplication([])

window = QMainWindow()


window.show()

sys.exit(app.exec())