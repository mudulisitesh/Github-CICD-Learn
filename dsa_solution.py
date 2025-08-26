Okay, here's a DSA problem with a Python solution:

**Problem:**

**Island Perimeter**

You are given a map in the form of a rectangular grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

**Example:**

```
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
```

**Explanation:**

The island consists of the 1s in the grid. We need to find its perimeter.

**Python Solution:**

```python
def islandPerimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid: A list of lists of integers representing the island grid.
              1 represents land, 0 represents water.

    Returns:
        The perimeter of the island.
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides of the land cell
                perimeter += 4

                # Subtract 1 for each neighboring land cell (horizontal/vertical only)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 1 for shared edge above and below
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 1 for shared edge left and right

    return perimeter

# Example Usage
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
perimeter = islandPerimeter(grid)
print(f"The island perimeter is: {perimeter}")  # Output: The island perimeter is: 16

grid2 = [[1]]
perimeter2 = islandPerimeter(grid2)
print(f"The island perimeter is: {perimeter2}")  # Output: The island perimeter is: 4

grid3 = [[1,0]]
perimeter3 = islandPerimeter(grid3)
print(f"The island perimeter is: {perimeter3}")  # Output: The island perimeter is: 4
```

**Explanation:**

1. **Initialization:**
   - `rows` and `cols`: Store the dimensions of the grid.
   - `perimeter`: Initialize the perimeter to 0.

2. **Iterate Through the Grid:**
   - The code iterates through each cell of the grid using nested loops.

3. **Check for Land:**
   - `if grid[i][j] == 1:`: If a cell is land (value 1), the algorithm proceeds to calculate its contribution to the perimeter.

4. **Initial Perimeter Calculation:**
   - `perimeter += 4`: Initially, each land cell is assumed to have a perimeter of 4 (all four sides are water).

5. **Subtract Shared Edges:**
   - The code then checks the adjacent cells (up and left) to see if they are also land.
   - `if i > 0 and grid[i - 1][j] == 1:`: Checks the cell above. If it's land, it means the current cell shares an edge with it.  We decrement the perimeter by 2 because there is a land connection above that eliminates an exposed border.  (1 edge from the current cell and 1 from the upper cell)
   - `if j > 0 and grid[i][j - 1] == 1:`: Checks the cell to the left. If it's land, it means the current cell shares an edge with it. We decrement the perimeter by 2 because there is a land connection to the left that eliminates an exposed border. (1 edge from the current cell and 1 from the cell on the left)

6. **Return Perimeter:**
   - After iterating through all the cells, the function returns the calculated `perimeter`.

**Time and Space Complexity:**

- **Time Complexity:** O(m * n), where 'm' is the number of rows and 'n' is the number of columns in the grid.  We iterate through each cell in the grid exactly once.
- **Space Complexity:** O(1).  The algorithm uses a constant amount of extra space, regardless of the size of the grid.  We only store a few integer variables.
