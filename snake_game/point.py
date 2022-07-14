from random import randint

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __other: object) -> bool:
        return self.x == __other.x and self.y == __other.y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

def generate_point(start_x, max_x, start_y, max_y) -> Point:
    return Point(randint(start_x, max_x), randint(start_y, max_y))
