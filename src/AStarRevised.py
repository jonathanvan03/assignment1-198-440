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

def compute_path(grid, open_list, closed_list, cells, end, track_explored):
    """Function to perform A* searches"""
    if not open_list.heap: # if there are no more cells in the heap, no path is possible
        return None
    
    current = open_list.pop() # pop the min f valued cell to expand
    closed_list.add((current.x, current.y)) # add current cell to closed_list since it is already expanded

    if track_explored:
        track_explored(current)

    if (current.x, current.y) == end: # if the end cell was reached return
        return current
    
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dx, dy = current.x + i, current.y + j

        if (dx, dy) not in cells: # ignore cells that are blocked
            continue
        if (dx, dy) in closed_list: # ignore cells that were already expanded
            continue
        
        new_g  = current.g + 1 
        neighbor = cells[(dx, dy)]

        if new_g < neighbor.g:
            neighbor.update(new_g, current)
            open_list.insert(neighbor)

    return 1


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
            return None, 0, start_time - time.time()
        else: 
            print(f"Nearest unblocked cell found at {start}")
        

    # if end cell is initially blocked
    if grid[end[0]][end[1]] == 1: 
        print("End cell is blocked, searching for nearest unblocked cell.")
        end = find_nearest_unblocked(grid, end)

        if not end: 
            print("No unblocked cell found.") 
            return None, 0, start_time - time.tim()
        else: 
            print(f"Nearest unblocked cell found at {end}")
        


    # initialize all unblocked cells before search starts
    rows, cols = len(grid), len(grid[0])
    cells = {
        (x, y): Cell(x, y, float('inf'), manhattan_distance((x, y), end))
        for x in range(rows) for y in range(cols) if grid[x][y] == 0
    }
   
    Cell.larger_g = larger_g # determine whether larger or smaller g is preferred for tiebreakers
    expanded = 0 # initialize counter
    current_pos = start
    start_time = time.time()

    # set start cell g-value to 0
    start_cell = cells[current_pos]
    start_cell.g = 0
    start_cell.f = start_cell.h  # Since f = g + h

    # initialize open and closed lists
    open_list = MinBinaryHeap()
    open_list.insert(start_cell)
    closed_list = set()
    path = None

    while True:
        # perform A* search by repeatedly calling compute_path()
        res = compute_path(grid, open_list, closed_list, cells, end, track_explored)
        expanded += 1

        if type(res) == Cell:
            path = reconstruct_path(res)
            break

        if res == None:
            print(f"No path found, total expanded nodes = {expanded}")
            break
        

    return path, expanded, time.time() - start_time



