"""State class"""
class State:
    def __init__(self, x, y, ):
        self.x = x
        self.y = y
        
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        
        self.pointer = None
        
    def update(self):
        self.f = self.g + self.h
    
    