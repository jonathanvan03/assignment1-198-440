import csv
import generate_gridworlds
from AStar import main

def test_astar():
    # Open a CSV file for writing
    with open('astar_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow([
            "GridWorld", "Smaller g-value Expanded", "Smaller Runtime", 
            "Larger g-value Expanded", "Larger Runtime", "Message", "Favors"
        ])

        for i in range(1, 51):
            grid_file = f"grids_txt/gridworld_{i}.txt"  # Corrected string formatting
            grid = generate_gridworlds.load_grid_from_txt(grid_file)

            start = (50, 50)
            goal = (100, 100)

            # Initialize variables for storing results
            message_smaller = ""
            message_larger = ""

            # Run A* with smaller g-values
            print(f"\nRunning A* search on grid {i} with smaller g-values...")
            path_smaller_g, expanded_smaller_g, runtime_smaller_g = main(grid, start, goal, prefer_larger_g=False)
            if not path_smaller_g:
                message_smaller = "No path to the goal exists."
            else:
                message_smaller = "Goal reached!"

            # Print smaller g-values results to terminal
            print(f"Smaller g-values: Expanded {expanded_smaller_g} cells, Runtime: {runtime_smaller_g:.4f} seconds")
            print(f"Message: {message_smaller}")

            # Run A* with larger g-values
            print(f"\nRunning A* search on grid {i} with larger g-values...")
            path_larger_g, expanded_larger_g, runtime_larger_g = main(grid, start, goal, prefer_larger_g=True)
            if not path_larger_g:
                message_larger = "No path to the goal exists."
            else:
                message_larger = "Goal reached!"

            # Print larger g-values results to terminal
            print(f"Larger g-values: Expanded {expanded_larger_g} cells, Runtime: {runtime_larger_g:.4f} seconds")
            print(f"Message: {message_larger}")

            # Determine which g-value is favored
            if expanded_smaller_g is not None and expanded_larger_g is not None:
                if expanded_smaller_g < expanded_larger_g:
                    favors = "smaller"
                elif expanded_larger_g < expanded_smaller_g:
                    favors = "larger"
                else:
                    favors = "N/A"  # If both values are equal
            else:
                favors = "N/A"  # If either value is missing (e.g., blocked cell or no path)

            # Print favors to terminal
            print(f"Favors: {favors}")

            # Write the results to the CSV file
            writer.writerow([
                f"{i}",
                expanded_smaller_g,
                f"{runtime_smaller_g:.4f}",
                expanded_larger_g,
                f"{runtime_larger_g:.4f}",
                message_smaller if message_smaller == message_larger else f"{message_smaller} / {message_larger}",
                favors
            ])

# Run the test
test_astar()