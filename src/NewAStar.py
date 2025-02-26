from BinaryHeap import MinBinaryHeap
from Cell import Cell
from collections import deque
import time 

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # global direction coordinates for observing adjacent cells

def manhattan_distance(a, b):
    """Function to compute the manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_nearest_unblocked(grid, coord):
    """Function to determine nearest unblocked cell if start cell is blocked."""
    # initializations
    queue = deque([coord])
    visited = set()
    visited.add(coord)

    while queue:
        x, y = queue.popleft() # extract x, and y coord

        for i, j in dir: # iterate through directions
            dx, dy = x + i, y + j

            if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and (dx, dy) not in visited: # if new coord is within bounds 
                if grid[dx][dy] == 0: # if new coord is unblocked
                    return (dx, dy)
                
                queue.append((dx, dy)) # add to queue to search from coord
                visited.add((dx, dy)) 
    return None # No unblocked cell found

def reconstruct_path(end_cell):
    """Function to reconstruct the shortest path after end cell is reached"""
    path = []
    current = end_cell
    while current:
        path.append((current.x, current.y))
        current = current.parent  # Move to parent cell
    path.reverse()  # Get path from start to goal
    return path

def compute_path(open_list, closed_list, cells, end_cell, track_explored, counter, expanded):
    """Function to perform A* search"""
    
    while open_list.heap and end_cell.g > open_list.peek().f:
        current = open_list.pop()
        closed_list.add((current.x, current.y))
        expanded += 1
        
        if track_explored:
            track_explored(current)
        
        for i, j in dir:
            dx, dy = current.x + i, current.y + j
            
            if (dx, dy) not in cells:
                continue
            if (dx, dy) in closed_list:
                continue
            
            neighbor = cells[(dx, dy)]
            
            if neighbor.search < counter:
                neighbor.g = float('inf')
                neighbor.search = counter
                
               
            if neighbor.g > current.g + 1:
                neighbor.update(current.g + 1, current)
                
                if open_list.contains(neighbor): open_list.remove(neighbor)
                open_list.insert(neighbor)
                   
            if neighbor.x == end_cell.x and neighbor.y == end_cell.y:
                end_cell.parent = current  
                return expanded
                    
    return expanded

def AStar_main(grid, start, end, larger_g = True, track_explored = None):
    # if the start and end are the same point
    if start[0] == end[0] and start[1] == end[1]: 
        print("Start and goal are the same. Shortest path = 0.")
        return [start], 0, 0
    
    # if starting cell is initially blocked
    if grid[start[0]][start[1]] == 1: 
        print("Start cell is blocked, searching for nearest unblocked cell.")
        start = find_nearest_unblocked(grid, start)

        if not start: 
            print("No unblocked cell found.") 
            return None, 0, 0
        else: 
            print(f"Nearest unblocked cell found at {start}")
        

    # if end cell is initially blocked
    if grid[end[0]][end[1]] == 1: 
        print("End cell is blocked, searching for nearest unblocked cell.")
        end = find_nearest_unblocked(grid, end)

        if not end: 
            print("No unblocked cell found.") 
            return None, 0, 0
        else: 
            print(f"Nearest unblocked cell found at {end}")
            
    # initialize all unblocked cells before search starts
    rows, cols = len(grid), len(grid[0])
    cells = {
        (x, y): Cell(x, y, None, manhattan_distance((x, y), end), larger_g)
        for x in range(rows) for y in range(cols) if grid[x][y] == 0
    }
    
    counter = 0
    expanded = 0
    path = 0
    start_cell = cells[start]
    end_cell = cells[end]
    end_cell.g = float('inf')
    start_time = time.time()
    while end_cell.g == float('inf'):
        counter += 1
        
        start_cell.search = counter
        end_cell.g = float('inf')
        end_cell.search = counter
        
        open_list = MinBinaryHeap()
        closed_list = set()
        
        start_cell.update(0)
        open_list.insert(start_cell)
        
        if len(open_list.heap) == 0: 
            print("Cannot reach target cell")
            return None, expanded, time.time() - start_time
        
        expanded = compute_path(open_list, closed_list, cells, end_cell, track_explored, counter, expanded)
        
        if end_cell.g == float('inf'):
            print("Cannot reach target cell")
            return None, expanded, time.time() - start_time
        
    path = reconstruct_path(end_cell)
    
        
    
    
        
    return path, expanded, time.time() - start_time
