"""State class"""
class State:
    def __init__(self, x, y, isBlocked, larger_g = True ):
        self.x = x
        self.y = y
        self.isBlocked = isBlocked # whether the state is actually blocked or not
        self.isObserved = False # whether the agent has observed that the state is blocked
        
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        
        self.larger_g = larger_g
        self.pointer = None
        self.search = 0
        
    def update(self):
        self.f = self.g + self.h
    
    def tieBreak(self):
        return 999 * self.f - self.g if self.larger_g else 999 * self.f + self.g
    
    def __lt__(self, other):
        if self.f == other.f:
            return self.tieBreak() < other.tieBreak()
        return self.f < other.f
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    
    
    
    
    