Okay, here's a problem and a Python solution:

**Problem:  Minimum Path Sum in a Triangle**

Given a triangle represented as a list of lists of integers, where each row `i` has `i+1` elements, find the minimum path sum from top to bottom.  At each step, you can only move to an adjacent node in the row below.  Adjacent nodes are defined as the node with the same index as the current node or the node with index one greater than the current node.

For example:

```
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `2 + 3 + 5 + 1 = 11`.

**Constraints:**

*   You can only move to the nodes directly below or below and to the right of the current node.
*   The triangle is non-empty.

**Python Solution (Dynamic Programming - Bottom-Up Approach):**

```python
def minimum_total(triangle):
    """
    Finds the minimum path sum from top to bottom of a triangle.

    Args:
        triangle: A list of lists of integers representing the triangle.

    Returns:
        The minimum path sum.
    """

    n = len(triangle)

    # dp[i][j] stores the minimum path sum to reach triangle[i][j]
    dp = [[0] * (i + 1) for i in range(n)]

    # Initialize the last row of dp with the values from the last row of the triangle
    dp[n - 1] = triangle[n - 1]

    # Iterate from the second-to-last row up to the top row
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            # The minimum path sum to reach triangle[i][j] is the value of triangle[i][j]
            # plus the minimum of the path sums to reach its two children in the next row
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])

    # The minimum path sum from top to bottom is stored in dp[0][0]
    return dp[0][0]


# Example usage
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

min_path_sum = minimum_total(triangle)
print(f"The minimum path sum is: {min_path_sum}")  # Output: 11

triangle2 = [[-10]]
min_path_sum2 = minimum_total(triangle2)
print(f"The minimum path sum for triangle2 is: {min_path_sum2}") #output: -10

triangle3 = [[-1],[2,3],[1,-1,-3]]
min_path_sum3 = minimum_total(triangle3)
print(f"The minimum path sum for triangle3 is: {min_path_sum3}") # output -1
```

**Explanation:**

1.  **Dynamic Programming (Bottom-Up):** The solution uses dynamic programming with a bottom-up approach.
2.  **`dp` array:**  `dp[i][j]` stores the minimum path sum to reach the element `triangle[i][j]` from the *bottom* of the triangle.
3.  **Initialization:** The last row of `dp` is initialized directly from the last row of the `triangle` because the minimum path sum to reach any element in the last row is simply its own value.
4.  **Iteration:** The code iterates from the second-to-last row (`n - 2`) up to the top row (0). For each element `triangle[i][j]`, the minimum path sum to reach it is calculated as the value of `triangle[i][j]` plus the minimum of the path sums to reach its two possible children in the next row: `dp[i + 1][j]` (directly below) and `dp[i + 1][j + 1]` (below and to the right).
5.  **Result:** Finally, `dp[0][0]` will contain the minimum path sum from the top to the bottom of the triangle.

**How it works conceptually:**

The algorithm builds up the `dp` table by considering all possible paths from the bottom row upwards.  At each step, it chooses the path that gives the minimum sum.  By the time it reaches the top, `dp[0][0]` holds the minimum possible path sum from the top to the bottom of the triangle. The bottom-up approach avoids redundant calculations because each subproblem (finding the minimum path to an element in the triangle) is solved only once and its result is stored in the `dp` array for later use.
