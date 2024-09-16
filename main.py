import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QMainWindow, QMenuBar, QTextBrowser, QDialog, QGridLayout, QLabel, QScrollArea, QProgressBar, QGraphicsOpacityEffect
from PyQt6.QtGui import QAction, QImage, QPixmap
from PyQt6.QtCore import QPropertyAnimation, Qt

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        layout = QVBoxLayout()
        self.label = QLabel()
        pixmap = QPixmap(path) #change to argc
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    path = sys.argv[1]

    print(path)

    window = ImageWindow()
    window.show()
    sys.exit(app.exec())
