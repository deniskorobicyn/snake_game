class Grid:
    def __init__(self, width, height, step) -> None:
        self.width = width
        self.height = height
        self.step = step
        self.max_x = int(width / step) - 1
        self.max_y = int(height / step) - 1