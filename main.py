import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from convert_for_tardek import Convert  # твой основной класс

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Convert()
    window.setWindowIcon(QIcon('icons.ico'))  # путь к иконке
    window.show()
    sys.exit(app.exec())