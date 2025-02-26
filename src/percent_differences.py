import numpy as np
from generate_gridworlds import load_grid_from_txt
from NewAStar import AStar_main

# Lists to store percentage differences
large_g_run, small_g_run = [], []
large_g_expanded, small_g_expanded = [], []

# Iterate through 50 grids
for i in range(1, 51):
    print(f"Loading grids_txt/gridworld_{i}.txt...\n")
    
    grid = load_grid_from_txt(f"grids_txt/gridworld_{i}.txt")
    start, goal = (0, 0), (100, 100)  # Adjust if needed

    print(f"Running A* on Grid {i}...")

    # Run A* with larger-g tie-breaking
    path_lg, expanded_lg, runtime_lg = AStar_main(grid, start, goal, larger_g=True)
    # Run A* with smaller-g tie-breaking
    path_sg, expanded_sg, runtime_sg = AStar_main(grid, start, goal, larger_g=False)

    print(f"Grid {i} Results:")
    print(f"Larger-G: Runtime = {runtime_lg:.4f}s, Expanded Nodes = {expanded_lg}")
    print(f"Smaller-G: Runtime = {runtime_sg:.4f}s, Expanded Nodes = {expanded_sg}\n")

    # Compare runtimes
    if runtime_lg != runtime_sg:  # Avoid division by zero
        if runtime_lg < runtime_sg:
            percent_diff = ((runtime_sg - runtime_lg) / runtime_sg) * 100
            large_g_run.append(percent_diff)
        else:
            percent_diff = ((runtime_lg - runtime_sg) / runtime_lg) * 100
            small_g_run.append(percent_diff)

    # Compare expanded nodes
    if expanded_lg != expanded_sg:
        if expanded_lg < expanded_sg:
            percent_diff = ((expanded_sg - expanded_lg) / expanded_sg) * 100
            large_g_expanded.append(percent_diff)
        else:
            percent_diff = ((expanded_lg - expanded_sg) / expanded_lg) * 100
            small_g_expanded.append(percent_diff)

# Compute average percentage differences
avg_large_g_run = np.mean(large_g_run) if large_g_run else 0
avg_small_g_run = np.mean(small_g_run) if small_g_run else 0
avg_large_g_expanded = np.mean(large_g_expanded) if large_g_expanded else 0
avg_small_g_expanded = np.mean(small_g_expanded) if small_g_expanded else 0

# ANSI escape codes
GREEN = "\033[92m"
RESET = "\033[0m"

# Print the final results
print("FINAL RESULTS")
print(f"Average % runtime improvement (Larger-G faster): {GREEN}{avg_large_g_run:.2f}%{RESET}")
print(f"Average % runtime improvement (Smaller-G faster): {GREEN}{avg_small_g_run:.2f}%{RESET}")
print(f"Average % fewer nodes expanded (Larger-G better): {GREEN}{avg_large_g_expanded:.2f}%{RESET}")
print(f"Average % fewer nodes expanded (Smaller-G better): {GREEN}{avg_small_g_expanded:.2f}%{RESET}")
