import matplotlib.pyplot as plt
import numpy as np
import time
from AStar import main
import generate_gridworlds

def visualize_astar(grid, start, goal, larger_g=False):
    """Visualize the A* search process in real-time."""

    fig, ax = plt.subplots()
    rows, cols = len(grid), len(grid[0])

    # Define color mapping
    cmap = {
        0: "white",  # Unblocked
        1: "black",  # Blocked
        2: "blue",   # Explored cells
        3: "red"     # Final path
    }

    # Convert grid to color format
    color_grid = np.array(grid, dtype=int)

    # Function to update the visualization
    def update_search():
        """Updates the visualization of the grid dynamically."""
        ax.clear()
        ax.imshow(color_grid, cmap=plt.cm.colors.ListedColormap([cmap[i] for i in cmap]), interpolation="none")
        plt.pause(1)  # Small delay for animation effect

    # Define function to track explored cells
    def track_explored(cell):
        color_grid[cell.x, cell.y] = 2  # Mark as explored (blue)
        update_search()  # Update visualization after each step

    # Run A* and collect explored nodes
    path = main(grid, start, goal, larger_g, track_explored = track_explored)

    # Draw final path in red
    for (x, y) in path:
        color_grid[x, y] = 3  # Mark final path as red
        update_search()  # Update visualization

    plt.show()

# Generate a sample grid
grid = generate_gridworlds.load_grid_from_txt("grids_txt/gridworld_1.txt")
    
start = (1, 7)
goal = (8, 12)
print(grid)
# Run visualization
visualize_astar(grid, start, goal)
