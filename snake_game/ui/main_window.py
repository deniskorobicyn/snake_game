from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QDialog
from const import DOWN, LEFT, RIGHT, UP
from ui.apple_render import AppleRender
from ui.snake_render import SnakeRender
from ui.grid_render import GridRender
from PyQt5.QtCore import QTimer, Qt
from game import Game
from grid import Grid

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.title = "Snake Game"
        self.grid = Grid(1500, 1500, 50)
        self.setFixedSize(self.grid.width, self.grid.height)

        self.timer = QTimer()
        self.timer.timeout.connect(self.play)

        self.game = Game(self.grid)
        self.grid_render = GridRender(self)
        self.snake_render = SnakeRender(self)
        self.apple_render = AppleRender(self)
 
        self.InitWindow()
 
 
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.grid.width, self.grid.height)
        self.show()
        self.timer.start(300)
 
 
    def paintEvent(self, e):
        self.grid_render.render()
        self.snake_render.render(self.game)
        self.apple_render.render(self.game)
        
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        key = event.key()
        if key == Qt.Key.Key_Up:
            self.game.change_direction(UP)    
        elif key == Qt.Key.Key_Down:
            self.game.change_direction(DOWN)
        elif key == Qt.Key.Key_Left:
            self.game.change_direction(LEFT)
        elif key == Qt.Key.Key_Right:
            self.game.change_direction(RIGHT)
        
        return super().keyPressEvent(event)
           
    def play(self):
        if self.game.play():
            self.update()
        else:
            print('you failed')
            self.game.restart()


 