import generate_gridworlds
from AStar import main

def test_astar():

    grid = generate_gridworlds.load_grid_from_txt("grids_txt/gridworld_1.txt")
    
    start = (2, 8)
    goal = (97, 97)

    print("Running A* search...")
    path = main(grid, start, goal, prefer_larger_g=False)

    if path:
        print("Path found:", path)
    else:
        print("No path found!")

# Run the test
test_astar()

