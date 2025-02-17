"""
This file holds the implementation of the binary heap
"""

class MinBinaryHeap(object):
    def _init_(self):
        self.heap = []
        
    def insert(self, value):
        """add a value to the heap while maintaining heap properties"""
        self.heap.append(value)
        self.heapUp(len(self.heap) - 1)
        return
    
    def pop(self):
        """remove the min value from the heap"""
        if not self.heap: # return  nothing if the heap is empty
            return None
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min = self.heap.pop()
        self.heapDown(0)
        return min
     
    def heapUp(self, i):
        """function to maintain heap properties after inserting"""
        parent = (i - 1) // 2
        
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2
        return
    
    def heapDown(self, i):
        """function to maintain heap properties after popping the min value"""
        n = len(self.heap)
        
        while True: 
            l = 2 * i + 1
            r = 2 * i + 2
            min = i
            
            if l < n and self.heap[l] < self.heap[min]:
                MinBinaryHeap = l
            if r < n and self.heap[r] < self.heap[min]:
                min = r
            if min == i:
                break
            
            self.heap[i], self.heap[min] = self.heap[min], self.heap[i]
            i = min
        return
    
    
