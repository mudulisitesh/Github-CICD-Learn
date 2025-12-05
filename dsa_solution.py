Okay, here's a random DSA problem, along with a Python solution:

**Problem:**

**Cycle Detection in a Directed Graph**

Given a directed graph represented as an adjacency list, determine if the graph contains a cycle.

**Input:**

*   `graph`: A dictionary (adjacency list) where keys represent nodes and values are lists of their neighbors. For example:
    ```python
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]  # Self-loop, which is also a cycle
    }
    ```

**Output:**

*   `True` if the graph contains a cycle, `False` otherwise.

**Explanation:**

A cycle exists in a directed graph if you can start at a node and follow a path of edges that eventually leads you back to the starting node.  You can solve this using Depth-First Search (DFS).  The main idea is to keep track of nodes that are currently in the recursion stack (being visited). If you encounter a node that is already in the recursion stack, you've found a cycle.

**Python Solution:**

```python
def has_cycle(graph):
    """
    Detects cycles in a directed graph using DFS.

    Args:
        graph: A dictionary representing the graph as an adjacency list.

    Returns:
        True if the graph contains a cycle, False otherwise.
    """

    def dfs(node, visited, recursion_stack):
        """
        Performs Depth-First Search starting from a node.

        Args:
            node: The current node being visited.
            visited: A set of visited nodes.
            recursion_stack: A set of nodes currently in the recursion stack.

        Returns:
            True if a cycle is detected, False otherwise.
        """

        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph.get(node, []):  # Iterate through neighbors
            if neighbor in recursion_stack:
                return True  # Cycle detected

            if neighbor not in visited:
                if dfs(neighbor, visited, recursion_stack):
                    return True  # Cycle detected in subtree

        recursion_stack.remove(node)  # Remove node from recursion stack when done
        return False  # No cycle found in this branch

    num_nodes = len(graph)
    visited = set()
    recursion_stack = set()

    for node in graph: # Iterate through all nodes to handle disconnected components
        if node not in visited:  # Ensure all components are explored
            if dfs(node, visited, recursion_stack):
                return True  # Cycle detected

    return False  # No cycle found in the entire graph


# Example Usage:
graph1 = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
print(f"Graph 1 has cycle: {has_cycle(graph1)}")  # Output: True

graph2 = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}
print(f"Graph 2 has cycle: {has_cycle(graph2)}")  # Output: False

graph3 = {
    0: [1],
    1: [2],
    2: [0]
}
print(f"Graph 3 has cycle: {has_cycle(graph3)}") # Output: True

graph4 = {
    0: [1],
    1: [2],
    2: [3],
    3: [4],
    4: []
}
print(f"Graph 4 has cycle: {has_cycle(graph4)}") # Output: False

graph5 = {
    0: [],
    1: []
}
print(f"Graph 5 has cycle: {has_cycle(graph5)}") # Output: False

graph6 = {
    0: [1],
    1: [0]
}

print(f"Graph 6 has cycle: {has_cycle(graph6)}") # Output: True
```

**Explanation of the Code:**

1.  **`has_cycle(graph)` Function:**
    *   Initializes `visited` (a set to keep track of visited nodes during the DFS traversal) and `recursion_stack` (a set to keep track of nodes currently in the recursion stack).
    *   Iterates through each node in the graph to handle cases where the graph might have disconnected components.  If a node hasn't been visited yet, it calls the `dfs()` function starting from that node.

2.  **`dfs(node, visited, recursion_stack)` Function:**
    *   Marks the current `node` as visited and adds it to the `recursion_stack`.
    *   Iterates through the neighbors of the current `node`.
    *   **Cycle Detection:** If a neighbor is already in the `recursion_stack`, it means we've encountered a back edge, indicating a cycle.  In this case, the function immediately returns `True`.
    *   **Recursive Call:** If a neighbor hasn't been visited yet, the `dfs()` function is called recursively on that neighbor. If the recursive call returns `True` (meaning a cycle was found in the subtree), the function also returns `True`.
    *   **Backtracking:** After visiting all neighbors of a node, the node is removed from the `recursion_stack`.  This is crucial for backtracking; we're indicating that we're no longer "exploring" that branch of the graph.
    *   **No Cycle Found:** If the function reaches the end without finding a cycle, it returns `False`.

**Key Concepts Used:**

*   **Depth-First Search (DFS):** A graph traversal algorithm that explores as far as possible along each branch before backtracking.
*   **Adjacency List:** A way to represent a graph where each node is associated with a list of its neighbors.
*   **Recursion Stack:** The data structure used to keep track of the function calls during recursive execution.  In this case, it's used to detect back edges, which indicate cycles.
*   **`visited` Set:**  This set prevents infinite loops by ensuring that each node is visited only once during the DFS traversal (except when a cycle is being detected).
*   **`recursion_stack` Set:** This set is critical for cycle detection.  It stores the nodes that are currently being explored in the current path of the DFS. If we encounter a node that is already in the recursion stack, it means we've found a back edge and thus a cycle.
This solution is efficient and handles disconnected graphs correctly.  It provides a clear and understandable implementation of cycle detection in a directed graph using DFS.  The example usage demonstrates the function's effectiveness with various graph structures.
