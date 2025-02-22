"""
This file holds the implementation of the binary heap
"""

class MinBinaryHeap(object):
    def __init__(self):
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
        minimum = self.heap.pop()
        self.heapDown(0)
        return minimum
     
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
            minimum = i
            
            if l < n and self.heap[l] < self.heap[minimum]:
                minimum = l
            if r < n and self.heap[r] < self.heap[minimum]:
                minimum = r
            if minimum == i:
                break
            
            self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
            i = minimum
        return
    
    
# heap = MinBinaryHeap()
# heap.insert(10)
# heap.insert(5)
# heap.insert(15)
# heap.insert(3)
# heap.insert(8)

# print(heap.heap)  # Expected: [3, 5, 15, 10, 8] or similar valid min-heap structure

# print(heap.pop())  # Expected: 3
# print(heap.heap)  # Expected: [5, 8, 15, 10]

# print(heap.pop())  # Expected: 5
# print(heap.heap)  # Expected: [8, 10, 15]
