class MinBinaryHeap:
    def __init__(self):
        self.heap = []
        self.position_map = {}  # Keeps track of element positions for O(1) lookup

    def insert(self, value):
        """Add a value to the heap while maintaining heap properties."""
        self.heap.append(value)
        self.position_map[(value.x, value.y)] = len(self.heap) - 1
        self.heapUp(len(self.heap) - 1)

    def pop(self):
        """Remove and return the min value from the heap."""
        if not self.heap:
            return None
        
        self.swap(0, len(self.heap) - 1)  # Swap root with last element
        min_val = self.heap.pop()
        self.position_map.pop((min_val.x, min_val.y), None)

        if self.heap:
            self.heapDown(0)  # Restore heap property

        return min_val

    def peek(self):
        """Return the min value without removing it."""
        return self.heap[0] if self.heap else None

    def contains(self, value):
        """Check if a value is in the heap."""
        return (value.x, value.y) in self.position_map

    def remove(self, value):
        """Remove a specific value from the heap if it exists."""
        if (value.x, value.y) not in self.position_map:
            return  # Value not found

        index = self.position_map.pop((value.x, value.y))  
        if index == len(self.heap) - 1:  
            self.heap.pop()  # Just remove last element
            return

        self.swap(index, len(self.heap) - 1)  # Swap with last element
        self.heap.pop()

        if index < len(self.heap):
            self.heapUp(index)
            self.heapDown(index)

    def heapUp(self, i):
        """Maintain heap property after inserting."""
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def heapDown(self, i):
        """Maintain heap property after popping."""
        n = len(self.heap)
        while True:
            l, r = 2 * i + 1, 2 * i + 2
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
        """Swap two elements in the heap and update position_map."""
        self.position_map[(self.heap[i].x, self.heap[i].y)] = j
        self.position_map[(self.heap[j].x, self.heap[j].y)] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
