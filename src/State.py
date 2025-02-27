"""State class"""
class State:
    def __init__(self, x, y, isBlocked):
        self.x = x
        self.y = y
        self.isBlocked = isBlocked # whether the state is actually blocked or not
        self.isObserved = False # whether the agent has observed that the state is blocked
        
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        
        self.pointer = None
        self.search = 0
        
    def update(self):
        self.f = self.g + self.h
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    
    
    
    
    