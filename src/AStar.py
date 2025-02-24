from BinaryHeap import MinBinaryHeap
from Cell import Cell
from collections import deque
import time  # For measuring runtime

def compute_path(grid, open_list, closed_set, cells, goal, track_explored):
    """Expands one node in the A* search process and returns the goal cell if reached."""
    expanded_cells = 0  # Counter for expanded cells

    if not open_list.heap:
        return None, expanded_cells  # No path found

    while open_list.heap:
        current = open_list.pop()  # Expand one node
        expanded_cells += 1  # Increment counter when a cell is expanded

        if (current.x, current.y) == goal:
            return current, expanded_cells  # Goal reached

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

    return None, expanded_cells  # Goal not reached yet

def find_nearest_unblocked(grid, start):
    """Find the nearest unblocked cell starting from the given position."""
    if grid[start[0]][start[1]] == 0:
        return start  

    # Directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                if grid[nx][ny] == 0:  # Unblocked cell
                    return (nx, ny)

                queue.append((nx, ny))
                visited.add((nx, ny))

    return None  # No unblocked cell found

def move_agent(grid, path, start, goal):
    """Simulates the agent moving along the path and updates the grid when blocked cells are encountered."""
    current_position = start
    for next_position in path[1:]:  # Skip the first cell (start position)
        x, y = next_position
        if grid[x][y] == 1:  # Blocked cell encountered
            print(f"Blocked cell encountered at {next_position}. Replanning...")
            grid[x][y] = 1  # Update the grid to mark the cell as blocked
            return current_position  # Return the last valid position
        current_position = next_position  # Move to the next cell
        # print(f"Moved to {current_position}")
    return current_position  # Return the final position (goal)

def main(grid, start, goal, prefer_larger_g=False, track_explored=None):
    """Repeated A*: Plans a path, moves the agent, and replans when blocked cells are encountered."""
    if grid[start[0]][start[1]] == 1:  # If start cell is blocked
        print("Start cell is blocked!")
        start = find_nearest_unblocked(grid, start)
        if not start:
            print("No unblocked start position found.")
            return None, 0, 0  # No path found, 0 expanded cells, 0 runtime
        else:
            print(f"Nearest unblocked start position found at {start}")

    if grid[goal[0]][goal[1]] == 1:  # If goal cell is blocked
        print("Goal cell is blocked!")
        return None, 0, 0  # No path found, 0 expanded cells, 0 runtime

    # Configure tie-breaking strategy
    Cell.larger_g = prefer_larger_g

    # Initialize all cells before search starts
    rows, cols = len(grid), len(grid[0])
    cells = {
        (x, y): Cell(x, y, float("inf"), manhattan_distance((x, y), goal))
        for x in range(rows) for y in range(cols)
    }

    current_position = start
    total_expanded_cells = 0  # Total number of expanded cells
    start_time = time.time()  # Start measuring runtime

    while current_position != goal:
        # Set start cell g-value to 0
        start_cell = cells[current_position]
        start_cell.g = 0
        start_cell.f = start_cell.h  # Since f = g + h

        # Open list (MinHeap) and Closed Set
        open_list = MinBinaryHeap()
        open_list.insert(start_cell)
        closed_set = set()

        # Perform A* search
        goal_cell, expanded_cells = compute_path(grid, open_list, closed_set, cells, goal, track_explored)

        total_expanded_cells += expanded_cells  # Accumulate expanded cells

        if goal_cell is None:
            print("No path to the goal exists.")
            return None, total_expanded_cells, time.time() - start_time  # No path found

        # Reconstruct path
        path = reconstruct_path(goal_cell)
        # print("Computed path:", path)

        # Simulate agent movement
        current_position = move_agent(grid, path, current_position, goal)

        if current_position == goal:
            print("Goal reached!")
            return path, total_expanded_cells, time.time() - start_time  # Path found

    return None, total_expanded_cells, time.time() - start_time  # No path found
  
def manhattan_distance(a, b):
    """Compute Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(goal_cell):
    """Reconstructs the shortest path from goal to start."""
    path = []
    current = goal_cell
    while current:
        path.append((current.x, current.y))
        current = current.parent  # Move to parent cell
    path.reverse()  # Get path from start to goal
    return path