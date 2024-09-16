import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QMainWindow, QMenuBar, QTextBrowser, QDialog, QGridLayout, QLabel, QScrollArea, QProgressBar, QGraphicsOpacityEffect
from PyQt6.QtGui import QAction, QImage, QPixmap
from PyQt6.QtCore import QPropertyAnimation, Qt

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")

        #self.setMaximumWidth(500)
        #self.setMaximumHeight(500) #in dev

        layout = QVBoxLayout()
        self.label = QLabel()
        pixmap = QPixmap(path)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        layout.addWidget(self.label)
        self.setLayout(layout)

        

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No path provided")
        sys.exit(1)

    app = QApplication(sys.argv)
    path = sys.argv[1]

    print(f"Path to image is {path}")

    window = ImageWindow()
    window.show()
    sys.exit(app.exec())
