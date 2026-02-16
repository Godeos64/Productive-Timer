import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

class MessageBox:
    def __init__(self, text, title="Message"):
        # Ensure a QApplication exists (crucial for standalone scripts)
        self.app = QApplication.instance() or QApplication(sys.argv)
        
        self.box = QMessageBox()
        self.box.setWindowTitle(title)
        self.box.setText(text)

    def show(self):
        self.box.exec()

# --- Usage ---
if __name__ == "__main__":
    # Reusable and configurable
    MessageBox("Database connection failed.", "Error").show()
    MessageBox("Operation completed successfully.").show()