from BinaryHeap import MinBinaryHeap
from Cell import Cell

def compute_path(grid, open_list, closed_set, cells, goal, track_explored):
    """Expands one node in the A* search process and returns the goal cell if reached."""
    
    if not open_list.heap:
        return None  # No path found

    current = open_list.pop()  # Expand one node

    if (current.x, current.y) == goal:
        return current  # Goal reached

    closed_set.add((current.x, current.y))

    if track_explored:
        track_explored(current)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = current.x + dx, current.y + dy

        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):  
            continue  # Out of bounds
        if grid[nx][ny] == 1:  
            continue  # Blocked cell
        if (nx, ny) in closed_set:  
            continue  # Already expanded

        new_g = current.g + 1  
        neighbor = cells[(nx, ny)]  # Get the pre-initialized Cell

        if new_g < neighbor.g:  # Found a better path
            neighbor.update(new_g, current)
            open_list.insert(neighbor)

    return None  # Goal not reached yet

def main(grid, start, goal, prefer_larger_g=False, track_explored=None):
    """Initializes A* search and iteratively calls compute_path()."""
    
    if grid[start[0]][start[1]] == 1:  #if blocked off of start
        print("Start cell is blocked!")
        start = find_nearest_unblocked(grid, start)
        if not start:
            print("No unblocked start position found.")
            return None  
        else:
            print(f"Nearest unblocked start position found at {start}")

    if grid[goal[0]][goal[1]] == 1:
        print("Goal cell is blocked!")
        return None 
        
    # Configure tie-breaking strategy
    Cell.prefer_larger_g = prefer_larger_g  

    # Initialize all cells **before search starts**
    rows, cols = len(grid), len(grid[0])
    cells = {
        (x, y): Cell(x, y, float("inf"), manhattan_distance((x, y), goal)) 
        for x in range(rows) for y in range(cols)
    }
    
    # Set start cell g-value to 0
    start_cell = cells[start]
    start_cell.g = 0
    start_cell.f = start_cell.h  # Since f = g + h

    # Open list (MinHeap) and Closed Set
    open_list = MinBinaryHeap()
    open_list.insert(start_cell)
    closed_set = set()

    # Keep calling compute_path() until goal is found
    goal_cell = None
    while goal_cell is None:
        goal_cell = compute_path(grid, open_list, closed_set, cells, goal, track_explored)

    # Return reconstructed path
    return reconstruct_path(goal_cell) if goal_cell else None

def manhattan_distance(a, b):
    """Compute Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(goal_cell):

    """Reconstructs the shortest path from goal to start."""
    print("Reconstructing path")
    path = []
    current = goal_cell

    print("Reconstructing path...")
    while current:
        path.append((current.x, current.y))
        current = current.parent  # Move to parent cell

    path.reverse()  # Get path from start to goal
    print("Final reconstructed path:", path)  # Print final path for verification
    return path
