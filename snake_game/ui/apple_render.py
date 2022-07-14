from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import QRect, Qt
from game import Game

class AppleRender:
    def __init__(self, window) -> None:
        self.parent_window = window
        self.grid = window.grid

    def render(self, game: Game) -> None:
        point = game.apple_state()
        painter = QPainter(self.parent_window)

        rect = QRect(
            self.grid.step * point.x, 
            self.grid.step * point.y, 
            self.grid.step, 
            self.grid.step, 
        )

        painter.fillRect(rect, QBrush(Qt.red))
        
        
