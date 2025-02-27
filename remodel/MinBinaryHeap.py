from State import State

class MinBinaryHeap:
    def __init__(self):
        self.heap = []
        self.coords = {}
            
    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def insert(self, state):
        self.heap.append(state)
        self.coords[(state.x, state.y)] = len(self.heap) - 1
        self.heapUp(len(self.heap) - 1)           
       
    def pop(self):
        if not self.heap:
            return None
        
        self.swap(0, len(self.heap) - 1)  # Swap root with last element
        min_val = self.heap.pop()
        self.coords.pop((min_val.x, min_val.y), None)

        if self.heap:
            self.heapDown(0)  # Restore heap property

        return min_val
    
    def remove(self, state):
        if (state.x, state.y) not in self.coords:
            return  # Value not found

        index = self.coords.pop((state.x, state.y))  
        if index == len(self.heap) - 1:  
            self.heap.pop()  # Just remove last element
            return

        self.swap(index, len(self.heap) - 1)  # Swap with last element
        self.heap.pop()

        if index < len(self.heap):
            self.heapUp(index)
            self.heapDown(index)
                
    def peek(self):
        return self.heap[0] if self.heap else None
                    
    def heapUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2
            
    def heapDown(self, i):
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
        self.coords[(self.heap[i].x, self.heap[i].y)] = j
        self.coords[(self.heap[j].x, self.heap[j].y)] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            
    def contains(self, state):
        if state in self.heap:
            return True
        else:
            return False 
            
            
def test_heap_operations():
    print("Starting MinBinaryHeap tests...\n")

    # Create a heap instance
    heap = MinBinaryHeap()

    # Create state objects with different f-values
    state1 = State(0, 0, False)  # f = 0
    state1.g, state1.h = 3, 5
    state1.update()  # f = 8

    state2 = State(1, 1, False)  # f = 0
    state2.g, state2.h = 2, 4
    state2.update()  # f = 6

    state3 = State(2, 2, False)  # f = 0
    state3.g, state3.h = 1, 2
    state3.update()  # f = 3

    state4 = State(3, 3, False)  # f = 0
    state4.g, state4.h = 4, 6
    state4.update()  # f = 10

    # Insert elements into heap
    print("Inserting states...")
    heap.insert(state1)
    heap.insert(state2)
    heap.insert(state3)
    heap.insert(state4)

    print("Heap contents after insertions:")
    for state in heap.heap:
        print(f"State ({state.x}, {state.y}): f = {state.f}, g = {state.g}, h = {state.h}")

    # Peek at the min element
    min_state = heap.peek()
    print(f"\nPeeked min state: ({min_state.x}, {min_state.y}) with f = {min_state.f}")
    assert min_state == state3, "Peek should return the state with the smallest f-value."

    # Pop elements and check order
    print("\nPopping elements...")
    while not heap.isEmpty():
        state = heap.pop()
        print(f"Popped ({state.x}, {state.y}): f = {state.f}")
    
    assert heap.isEmpty(), "Heap should be empty after all pops."

    # Insert elements again for remove() test
    heap.insert(state1)
    heap.insert(state2)
    heap.insert(state3)
    heap.insert(state4)

    print("\nRemoving state (1,1)...")
    heap.remove(state2)  # Remove state2 (f = 6)
    
    print("Heap contents after removal:")
    for state in heap.heap:
        print(f"State ({state.x}, {state.y}): f = {state.f}, g = {state.g}, h = {state.h}")

    assert state2 not in heap.heap, "State (1,1) should be removed from the heap."

    print("\nAll tests passed! 🎉")

if __name__ == "__main__":
    test_heap_operations()