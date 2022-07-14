from typing import List
import random
from grid import Grid
from point import Point, generate_point
from const import DOWN, LEFT, RIGHT, UP, EATEN, HIT, EMPTY

class Snake:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.default_size = 4
        self.direction = random.choice([RIGHT, DOWN])
        self.pieces = self.__initialize_pieces()

    def move(self, apple) -> bool:
        old_head = self.pieces[0]
        if self.direction == UP:
            new_head = Point(old_head.x, old_head.y - 1)
        elif self.direction == DOWN:
            new_head = Point(old_head.x, old_head.y + 1)
        elif self.direction == LEFT:
            new_head = Point(old_head.x - 1, old_head.y)
        elif self.direction == RIGHT:
            new_head = Point(old_head.x + 1, old_head.y)

        print(self)
        print(self.direction)
        if new_head != apple:
            if new_head in self or \
                new_head.x > self.grid.max_x or \
                new_head.y > self.grid.max_y or \
                new_head.x < 0 or \
                new_head.y < 0:
                return HIT

            for piece_num in range(len(self.pieces) - 1, 0, -1):
                self.pieces[piece_num] = self.pieces[piece_num - 1]

            self.pieces[0] = new_head
            return EMPTY
        else:
            self.pieces.insert(0, new_head)
            return EATEN

    def change_direction(self, action) -> None:
        if (action == UP and self.direction == DOWN) or \
            (action == LEFT and self.direction == RIGHT) or \
            (action == RIGHT and self.direction == LEFT) or \
            (action == DOWN and self.direction == UP):
            return

        self.direction = action

    def __contains__(self, point: Point) -> bool:
        return point in self.pieces
    
    def __str__(self) -> str:
        return ' '.join(map(lambda x: str(x), self.pieces))

    def __initialize_pieces(self) -> List[Point]:
        head = generate_point(self.default_size + 1, self.grid.max_x, self.default_size + 1, self.grid.max_y)

        list = [head]

        if self.direction == RIGHT:
            for i in range(self.default_size):
                list.append(Point(head.x - i, head.y))
        else:
            for i in range(self.default_size):
                list.append(Point(head.x, head.y - i))

        return list
