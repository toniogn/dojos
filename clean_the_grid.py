import numpy as np
from typing import List, Tuple

class Square:
    def __init__(self, x: int, y: int, occupied: bool = False) -> None:
        self.x = x
        self.y = y
        self.cleaned = False
        self.occupied = occupied
        self.tetas = []

    def clean(self, teta: float):
        self.cleaned = True
        self.tetas.append(teta)

    def __repr__(self) -> str:
        return f"Square({self.x}, {self.y}, {self.occupied})"

class Robot:
    def __init__(self, grid: List[str]) -> None:
        self.squares = np.array([[Square(x, y, char == "x") for x, char in enumerate(row)] for y, row in enumerate(grid)])
        self.square = self.squares[0, 0]
        self.teta = 0

    def __get_next_coordinates(self) -> Tuple[int, int]:
        return int(self.square.x + np.cos(self.teta)), int(self.square.y + np.sin(self.teta))

    def get_next_square_forward(self) -> Square:
        next_x, next_y = self.__get_next_coordinates()
        try:
            next_square = self.squares[next_y, next_x]
        except IndexError:
            self.teta += np.pi / 2
            next_square = self.get_next_square_forward()
        else:
            if next_x < 0 or next_y < 0:
                self.teta += np.pi / 2
                next_square = self.get_next_square_forward()
        if next_square.occupied:
            self.teta += np.pi / 2
            next_square = self.get_next_square_forward()
        return next_square

    def clean(self):
        while not (
            self.square.cleaned
            and any(int(np.sin(self.teta)) == int(np.sin(teta)) for teta in self.square.tetas)
        ):  
            print(self.square, np.sin(self.teta), [np.sin(teta) for teta in self.square.tetas])
            self.square.clean(self.teta)
            self.square = self.get_next_square_forward()

    def count(self):
        return sum([square.cleaned for row in self.squares for square in row])

if __name__ == "__main__":
    a = Robot(["......", "....xx", "......"])
    a.clean()
    print(a.count())
