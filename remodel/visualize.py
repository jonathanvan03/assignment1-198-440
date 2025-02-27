import numpy as np
import matplotlib.pyplot as plt
from GenerateGridWorlds import load_grid_from_txt
from ForwardRepeatedAStar import repeatedForwardMain

def plot_shortest_path(grid_path, shortest_path):
    """Function to visualize the grid and color the shortest path states differently"""
    grid = load_grid_from_txt(grid_path)
    grid = np.array(grid)

    # Create a color map where:
    # 0 (unblocked) -> white
    # 1 (blocked) -> black
    # Path -> colored (light blue)
    cmap = plt.cm.binary
    norm = plt.Normalize(vmin=0, vmax=2)

    # Convert path states to a different value (e.g., 2) for coloring
    for r, c in shortest_path:
        grid[r][c] = 2  # Assign a new value for path visualization

    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap=cmap, norm=norm, origin='upper')

    # Mark the start and goal points
    plt.text(shortest_path[0][1], shortest_path[0][0], 'S', fontsize=12, color='green', ha='center', va='center', fontweight='bold')
    plt.text(shortest_path[-1][1], shortest_path[-1][0], 'G', fontsize=12, color='blue', ha='center', va='center', fontweight='bold')

    plt.title("Shortest Path Visualization")
    plt.xticks([])
    plt.yticks([])
    plt.show()

# Example usage
grid_path = "grids_txt/gridworld_1.txt"
start, goal = (0, 0), (100, 100)
shortest_path, expanded, time = repeatedForwardMain(grid_path, start, goal, True)
plot_shortest_path(grid_path, shortest_path)
print(shortest_path)
