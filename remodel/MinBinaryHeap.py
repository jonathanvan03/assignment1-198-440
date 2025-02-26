from State import State

class MinBinaryHeap:
    def __init__(self, larger_g):
        self.heap = []
        self.larger_g = larger_g
        
    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def heapUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2
            
    def heapDown(self, i):
        n = len(self.heap)
        while True:
            l, r = 2 * i + 1, 2 + i + 2
            smallest = i
            
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            
            self.swap(i, smallest)
            i = smallest
    
    def swap(self, i, j):
        self.position_map[(self.heap[i].x, self.heap[i].y)] = j
        self.position_map[(self.heap[j].x, self.heap[j].y)] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            