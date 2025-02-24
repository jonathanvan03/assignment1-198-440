import generate_gridworlds
from AStar import main

def test_astar():

    grid = generate_gridworlds.load_grid_from_txt("grids_txt/gridworld_1.txt")
    
    start = (1, 8)
    goal = (1, 12)

    print("Running A* search with smaller g-values...")
    path_smaller_g, expanded_smaller_g, runtime_smaller_g = main(grid, start, goal, prefer_larger_g=False)
    print(f"Smaller g-values: Expanded {expanded_smaller_g} cells, Runtime: {runtime_smaller_g:.4f} seconds")

    print("Running A* search with larger g-values...")
    path_larger_g, expanded_larger_g, runtime_larger_g = main(grid, start, goal, prefer_larger_g=True)
    print(f"Larger g-values: Expanded {expanded_larger_g} cells, Runtime: {runtime_larger_g:.4f} seconds")

# Run the test
test_astar()