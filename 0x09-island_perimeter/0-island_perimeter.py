#!/usr/bin/python3
"""
A module: defines a function that calculates
the perimeter of an island on a given grid
"""

def island_perimeter(grid):
    """
    Returns the perimeter of any notable island in the given grid
    """
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4  # Count 4 sides for each land cell

                # Check left cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for shared side
                
                # Check upper cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for shared side

    return perimeter