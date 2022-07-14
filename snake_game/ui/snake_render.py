from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import QRect, Qt
from game import Game

class SnakeRender:
    def __init__(self, window) -> None:
        self.parent_window = window
        self.grid = window.grid

    def render(self, game: Game) -> None:
        snake = game.snake_state()
        painter = QPainter(self.parent_window)

        for point in snake:
            painter.setPen(QPen(Qt.green))
            rect = QRect(
                self.grid.step * point.x, 
                self.grid.step * point.y, 
                self.grid.step, 
                self.grid.step, 
            )

            painter.fillRect(rect, QBrush(Qt.green))
        
