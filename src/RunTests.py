import numpy as np
import matplotlib.pyplot as plt
import time
from AStarRevised import AStar_main  # Ensure AStar_main is correctly imported
from generate_gridworlds import load_grid_from_txt  # Function to load individual grids

# Number of grids
num_grids = 50

# Lists to store runtimes and expanded nodes
larger_g_runtimes = []
smaller_g_runtimes = []
larger_g_expanded = []
smaller_g_expanded = []

# ANSI escape codes for colors
GREEN = "\033[92m"  # Success (Green)
RED = "\033[91m"    # Failure (Red)
RESET = "\033[0m"   # Reset color

# Run tests for each grid
for i in range(1, num_grids + 1):
    grid_filename = f"grids_txt/gridworld_{i}.txt"
    print(f"Loading {grid_filename}...")

    # Load grid
    grid = load_grid_from_txt(grid_filename)

    # Define start and goal positions (adjust if necessary)
    start, goal = (0, 0), (100, 100)

    print(f"\nRunning A* on Grid {i}...")

    # Run A* with larger-g tie-breaking
    path_larger_g, expandedl, runtime_larger_g = AStar_main(grid, start, goal, True)
    larger_g_runtimes.append(runtime_larger_g)
    larger_g_expanded.append(expandedl)

    # Run A* with smaller-g tie-breaking
    path_smaller_g, expandeds, runtime_smaller_g = AStar_main(grid, start, goal, False)
    smaller_g_runtimes.append(runtime_smaller_g)
    smaller_g_expanded.append(expandeds)

    # Determine if paths were found
    status_larger_g = f"{GREEN}Success{RESET}" if path_larger_g else f"{RED}Fail{RESET}"
    status_smaller_g = f"{GREEN}Success{RESET}" if path_smaller_g else f"{RED}Fail{RESET}"

    print(f"Grid {i}: Larger-g: {runtime_larger_g:.4f}s - {status_larger_g}, Smaller-g: {runtime_smaller_g:.4f}s - {status_smaller_g}")
    print(f"Expanded: Larger - {expandedl}, Smaller - {expandeds}")

# Convert lists to numpy arrays
grid_indices = np.arange(1, num_grids + 1)
bar_width = 0.4  # Space bars side by side

# Create subplots for runtime and expanded nodes
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Bar Graph for Runtime
axes[0].bar(grid_indices - bar_width/2, larger_g_runtimes, bar_width, label="Larger g", color="royalblue")
axes[0].bar(grid_indices + bar_width/2, smaller_g_runtimes, bar_width, label="Smaller g", color="orange")
axes[0].set_ylabel("Runtime (seconds)")
axes[0].set_title("A* Search Runtime Comparison: Larger-g vs. Smaller-g Tie-Breaking")
axes[0].legend()
axes[0].set_xticks(grid_indices)
axes[0].set_xticklabels(grid_indices, rotation=90)
axes[0].grid(axis="y", linestyle="--", alpha=0.7)

# Bar Graph for Expanded Nodes
axes[1].bar(grid_indices - bar_width/2, larger_g_expanded, bar_width, label="Larger g", color="royalblue")
axes[1].bar(grid_indices + bar_width/2, smaller_g_expanded, bar_width, label="Smaller g", color="orange")
axes[1].set_xlabel("Grid Number")
axes[1].set_ylabel("Cells Expanded")
axes[1].set_title("A* Search Cell Expansion Comparison: Larger-g vs. Smaller-g")
axes[1].legend()
axes[1].set_xticks(grid_indices)
axes[1].set_xticklabels(grid_indices, rotation=90)
axes[1].grid(axis="y", linestyle="--", alpha=0.7)

# Save the plots
plt.tight_layout()
plt.savefig("graphics/g_tiebreaking_comparison_bar.png")
plt.show()
