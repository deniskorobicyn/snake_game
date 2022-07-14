from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class GridRender:
    def __init__(self, parent_window) -> None:
        #TODO: figure out how to delegate properly
        self.grid = parent_window.grid
        self.parent_window = parent_window
        self.width = self.grid.max_x + 1
        self.height = self.grid.max_y + 1
        self.step = self.grid.step

    def render(self) -> None:
        painter = QPainter(self.parent_window)
        
        painter.setPen(Qt.black)

        for i in range(self.width):
            painter.drawLine(0, self.step * i, self.width * self.step, self.step * i)
        
        for i in range(self.height):
            painter.drawLine(self.step * i, 0, self.step * i, self.height * self.step)