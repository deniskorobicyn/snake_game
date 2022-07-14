from PyQt5.QtWidgets import QApplication
import sys
from ui.main_window import MainWindow
 
def main():
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()