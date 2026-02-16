import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt

def MessageBox(text, title="Message"):
    app = QApplication.instance() or QApplication(sys.argv)
    box = QMessageBox()
    box.setWindowTitle(title)
    box.setText(text)
    box.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint) # Forces Topmost
    box.setStyleSheet("QMessageBox{background:#2b2b2b;} QLabel{color:white;} QPushButton{background:#444;color:white;padding:5px;}")
    box.exec()

# Usage
MessageBox("I am always on top.", "Dark Mode")
