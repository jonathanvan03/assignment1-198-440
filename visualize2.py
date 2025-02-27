import matplotlib.pyplot as plt
import numpy as np
import time
from ForwardRepeatedAStar import repeatedForwardMain
from BackwardRepeatedAStar import repeatedBackwardMain
from AdaptiveAStar import repeatedAdaptiveMain
import GenerateGridWorlds

def visualize_astar(grid, grid_path, start, goal, larger_g=False):
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
        plt.pause(0.0000001)  # Small delay for animation effect

    # Define function to track explored cells
    def track_explored(cell):
        if grid[cell.x][cell.y] == 0: 
            color_grid[cell.x, cell.y] = 2  
            update_search()

    # Function to run A* and visualize the process
    def run_and_visualize(algorithm, algorithm_name):
        print(f"Running {algorithm_name}...")
        color_grid[:] = np.array(grid, dtype=int)  # Reset the color grid
        path, expanded_cells, runtime = algorithm(grid_path, start, goal, larger_g, track_explored=track_explored)
        print(f"Path: {path}")
        print(f"Number of expanded cells: {len(expanded_cells)}")
        print(f"Runtime: {runtime} seconds")

        if path is None:
            print(f"No path found using {algorithm_name}! The goal is blocked or unreachable.")
            update_search()
            return

        # Draw final path in red
        for (x, y) in path:
            color_grid[x, y] = 3  # Mark final path as red
            update_search()  # Update visualization

    # Run Forward A* and visualize
    run_and_visualize(repeatedForwardMain, "Repeated Forward A*")
    plt.pause(1.0)

    # Run Backward A* and visualize
    run_and_visualize(repeatedBackwardMain, "Repeated Backward A*")
    plt.pause(1.0)

    # Run Adaptive A* and visualize
    run_and_visualize(repeatedAdaptiveMain, "Repeated Adaptive A*")

    plt.show()

# Generate a sample grid
grid_path = "grids_txt/gridworld_1.txt"  # Path to the grid file
grid = GenerateGridWorlds.load_grid_from_txt(grid_path)

start = (0, 0)
goal = (100, 100)

# Run visualization
visualize_astar(grid, grid_path, start, goal, False)