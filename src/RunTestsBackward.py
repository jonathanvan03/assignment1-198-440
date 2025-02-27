import numpy as np
import matplotlib.pyplot as plt
import time
from GenerateGridWorlds import load_grid_from_txt  # Function to load individual grids
from ForwardRepeatedAStar import repeatedForwardMain
from BackwardRepeatedAStar import repeatedBackwardMain

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


    # Define start and goal positions (adjust if necessary)
    start, goal = (0, 0), (100, 100)

    print(f"\nRunning A* on Grid {i}...")

    # Run A* with larger-g tie-breaking
    path_larger_g, expandedl, runtime_larger_g = repeatedForwardMain(grid_filename, start, goal, True)
    # path_larger_g, expandedl, runtime_larger_g = main(grid, start, goal, True)

    larger_g_runtimes.append(runtime_larger_g)
    larger_g_expanded.append(len(expandedl))

    # Run A* with smaller-g tie-breaking
    path_smaller_g, expandeds, runtime_smaller_g = repeatedBackwardMain(grid_filename, start, goal, True) ## repeatedAdaptiveMain, True
    # path_smaller_g, expandeds, runtime_smaller_g = main(grid, start, goal, False)

    smaller_g_runtimes.append(runtime_smaller_g)
    smaller_g_expanded.append(len(expandeds))

    # Determine if paths were found
    status_larger_g = f"{GREEN}Success{RESET}" if path_larger_g else f"{RED}Fail{RESET}"
    # print("path:", path_larger_g)
    status_smaller_g = f"{GREEN}Success{RESET}" if path_smaller_g else f"{RED}Fail{RESET}"
    
    ## change labels (larger - forward; smaller - adaptive)
    print(f"Grid {i}: Forward: {runtime_larger_g:.4f}s - {status_larger_g}, Adaptive: {runtime_smaller_g:.4f}s - {status_smaller_g}")
    print(f"Expanded: Forward - {len(expandedl)}, Adaptive - {len(expandeds)}")

# Example data
grid_indices = np.arange(1, num_grids + 1)
bar_width = 0.4  

# Create subplots for runtime and expanded nodes
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Bar Graph for Runtime
axes[0].bar(grid_indices - bar_width/2, larger_g_runtimes, bar_width, label="Forward A*", color="royalblue")
axes[0].bar(grid_indices + bar_width/2, smaller_g_runtimes, bar_width, label="Backward A*", color="orange")
axes[0].set_xlabel("Grid Number")
axes[0].set_ylabel("Runtime (seconds)")
axes[0].set_title("Search Runtime Comparison: Forward A* vs. Backward A*")
axes[0].legend()
axes[0].set_xticks(grid_indices)
axes[0].set_xticklabels(grid_indices, rotation=90)
## Set 10 evenly spaced y-ticks for runtime
max_runtime = max(max(larger_g_runtimes), max(smaller_g_runtimes))
y_ticks_runtime = np.linspace(0, max_runtime, 10)
axes[0].set_yticks(y_ticks_runtime)
axes[0].grid(axis="y", linestyle="--", alpha=0.7)

# Bar Graph for Expanded Nodes
axes[1].bar(grid_indices - bar_width/2, larger_g_expanded, bar_width, label="Forward A*", color="royalblue")
axes[1].bar(grid_indices + bar_width/2, smaller_g_expanded, bar_width, label="Backward A*", color="orange")
axes[1].set_xlabel("Grid Number")
axes[1].set_ylabel("Cells Expanded")
axes[1].set_title("Cell Expansion Comparison: Forward A* vs. Backward A*")
axes[1].legend()
axes[1].set_xticks(grid_indices)
axes[1].set_xticklabels(grid_indices, rotation=90)
# Set 10 evenly spaced y-ticks for expanded nodes
max_expanded = max(max(larger_g_expanded), max(smaller_g_expanded))
y_ticks_expanded = np.linspace(0, max_expanded, 10)
axes[1].set_yticks(y_ticks_expanded)
axes[1].grid(axis="y", linestyle="--", alpha=0.7)

# Save the plots
plt.tight_layout()
plt.savefig("graphics/forwardVsBackward.png")
plt.show()