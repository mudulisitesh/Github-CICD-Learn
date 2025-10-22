Okay, here's a DSA problem and its Python solution.

**Problem:**

**Minimum Cost to Connect All Points**

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.  The cost to connect two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

**Example:**

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Explanation:
We can connect the points as follows:
- Connect [0,0] with [2,2] at cost |0-2| + |0-2| = 4
- Connect [2,2] with [5,2] at cost |2-5| + |2-2| = 3
- Connect [5,2] with [7,0] at cost |5-7| + |2-0| = 4
- Connect [2,2] with [3,10] at cost |2-3| + |2-10| = 9
The total cost of this connection is 4 + 3 + 4 + 9 = 20
```

**Solution (Python using Prim's Algorithm):**

```python
import heapq

def min_cost_connect_points(points):
    """
    Finds the minimum cost to connect all points using Manhattan distance.

    Args:
        points: A list of tuples representing the (x, y) coordinates of the points.

    Returns:
        The minimum cost to connect all points.
    """

    n = len(points)
    if n <= 1:
        return 0  # Nothing to connect if there's only one or zero points

    # Calculate Manhattan distance between two points
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # Prim's algorithm
    visited = set()
    min_cost = 0
    heap = [(0, 0)]  # (cost, point_index)  Start at point 0 with cost 0

    while len(visited) < n:
        cost, i = heapq.heappop(heap)

        if i in visited:
            continue

        visited.add(i)
        min_cost += cost

        for j in range(n):
            if j not in visited:
                distance = manhattan_distance(points[i], points[j])
                heapq.heappush(heap, (distance, j))

    return min_cost


# Example usage
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
result = min_cost_connect_points(points)
print(f"Minimum cost to connect all points: {result}")  # Output: 20

points2 = [[3,12],[-2,5],[-4,1]]
result2 = min_cost_connect_points(points2)
print(f"Minimum cost to connect all points: {result2}") # Output: 18
```

**Explanation:**

1. **Manhattan Distance:** The `manhattan_distance` function calculates the distance between two points as specified in the problem description.

2. **Prim's Algorithm:** This algorithm is used to find the Minimum Spanning Tree (MST) of the graph formed by the points. Each point is a node, and the weight of the edge between two points is the Manhattan distance.

   - `visited`: A set to keep track of the points that have already been included in the MST.

   - `min_cost`:  The total cost of the MST (initialized to 0).

   - `heap`:  A min-heap (priority queue) used to store the edges that can be added to the MST.  It stores tuples of the form `(cost, point_index)`, where `cost` is the Manhattan distance to the `point_index` from the MST.  We start with a cost of 0 at point 0.

   - **Loop:** The `while` loop continues until all points are in the MST (`len(visited) == n`).

     - `heapq.heappop(heap)`:  Extracts the edge with the minimum cost from the heap.

     - **Check if visited:** If the point `i` has already been visited, skip it.

     - **Add to MST:**  Add the point `i` to the `visited` set and increment `min_cost` by the `cost` of the edge.

     - **Update Heap:**  Iterate through all the other points `j` that have not yet been visited.  Calculate the Manhattan distance between `points[i]` and `points[j]`.  Add the edge `(distance, j)` to the heap. This ensures that the heap always contains the shortest edge to an unvisited point from the current MST.

3. **Return `min_cost`:** After the loop finishes, `min_cost` contains the total cost of the MST, which is the minimum cost to connect all the points.

**Time Complexity:** O(n^2 log n), where n is the number of points. The `n^2` comes from calculating the Manhattan distances, and the `log n` comes from the heap operations.
**Space Complexity:** O(n)  due to the `visited` set and the heap. In the worst case, the heap might contain all edges, so it can take up O(n^2) space if we don't handle duplicates well, but in practice, it will be closer to O(n).
This solution provides a clear and efficient way to solve the problem using Prim's algorithm.  It prioritizes readability and addresses the problem requirements directly.
