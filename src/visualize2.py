import matplotlib.pyplot as plt
import numpy as np
import time
from ForwardRepeatedAStar import repeatedForwardMain
import GenerateGridWorlds

def visualize_astar(grid, path, start, goal, larger_g=False): # change to true/false
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
        # plt.pause(0.000001)  # Small delay for animation effect
        plt.pause(0.0000001)  # Small delay for animation effect

    # Define function to track explored cells
    def track_explored(cell):
        if grid[cell.x][cell.y] == 0: 
            color_grid[cell.x, cell.y] = 2  
            update_search()

    # Run A* and collect explored nodes
    # path, expanded_cells, runtime = main(grid, start, goal, larger_g, track_explored=track_explored)
    path, expanded_cells, runtime = repeatedForwardMain(path, start, goal, larger_g, track_explored=track_explored)
    print(path)
    print(len(expanded_cells))
    print(runtime)
    # Check if a path was found
    if path is None:
        print("No path found! The goal is blocked or unreachable.")
        update_search() 
        plt.show()
        return

    # Draw final path in red
    for (x, y) in path:
        color_grid[x, y] = 3  # Mark final path as red
        update_search()  # Update visualization

    plt.show()

# Generate a sample grid
path = "grids_txt/gridworld_1.txt"
grid = GenerateGridWorlds.load_grid_from_txt(path)

  
start = (0 , 0)
goal = (100, 100)
# print(grid)

# Run visualization
visualize_astar(grid, path , start, goal, True)