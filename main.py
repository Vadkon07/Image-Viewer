import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap, QAction
from PyQt6.QtCore import Qt

class ImageWindow(QMainWindow):
    def __init__(self, file_path=None):
        super().__init__()
        self.setWindowTitle("Image Viewer")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel()
        self.layout.addWidget(self.label)

        self.create_menu()

        if file_path:
            self.display_image(file_path)

    def create_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        screen_rect = QApplication.primaryScreen().availableGeometry()
        max_width = int(screen_rect.width() * 0.8)
        max_height = int(screen_rect.height() * 0.8)

        # Scale the pixmap to fit within the maximum dimensions
        pixmap = pixmap.scaled(max_width, max_height, Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    file_path = sys.argv[1] if len(sys.argv) > 1 else None

    window = ImageWindow(file_path)
    window.show()
    sys.exit(app.exec())

