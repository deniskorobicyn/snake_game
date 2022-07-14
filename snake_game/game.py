from typing import List
from snake import Snake
from point import Point, generate_point
from const import EATEN, HIT

class Game:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.restart()

    def play(self) -> bool:
        result = self.snake.move(self.apple)
        if result == EATEN:
            self.apple = self.__generate_apple()
            return True
        elif result == HIT:
            return False
        else:
            return True

    def restart(self):
        self.snake = Snake(self.grid)
        self.apple = self.__generate_apple()

    def change_direction(self, action):
        self.snake.change_direction(action)

    def snake_state(self) -> List[Point]:
        return self.snake.pieces

    def apple_state(self) -> Point:
         return self.apple

    def __generate_apple(self) -> Point:
        for i in range(10):
            apple_candidate = generate_point(
                self.snake.default_size + 1, 
                self.grid.max_x,
                self.snake.default_size + 1,
                self.grid.max_y
            )

            if apple_candidate not in self.snake:
                return apple_candidate

        return apple_candidate



