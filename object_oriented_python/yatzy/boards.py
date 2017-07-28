"""Create a new Board subclass named TicTacToe. 
Have it automatically be a 3x3 board by automatically setting values in the __init__.
Now make all Board instances iterable so we can loop through their cells attribute. """


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height= height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))


class TicTacToe(Board):
    def __init__(self):
        super().__init__(width=3, height=3)

    def __iter__(self):
        for item in self.cells:
            yield item


t = TicTacToe()
print(t.cells)
