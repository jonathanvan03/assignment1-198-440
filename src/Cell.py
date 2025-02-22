class Cell:

    larger_g = False

    def __init__(self, x, y, g, h, parent = None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        if self.f == other.f:
            return self.g > other.g if Cell.larger_g else self.g < other.g
        return self.f < other.f
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def update(self, new_g, new_parent):
        self.g = new_g
        self.f = self.g + self.h
        self.parent = new_parent

