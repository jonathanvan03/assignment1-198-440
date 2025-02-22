class Cell:
    def __init__(self, x, y, g, h, parent = None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __