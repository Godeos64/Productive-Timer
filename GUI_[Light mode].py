import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt

def MessageBox(text, title="Message"):
    app = QApplication.instance() or QApplication(sys.argv)
    box = QMessageBox()
    box.setWindowTitle(title)
    box.setText(text)
    box.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint) # Forces Topmost
    # No stylesheet needed for native Light Mode look
    box.exec()

# Usage
# MessageBox("I am always on top.", "Light Mode")
