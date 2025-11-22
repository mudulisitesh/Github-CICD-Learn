Okay, here's a problem involving trees and a solution in Python.

**Problem:**

**Binary Tree Level Order Traversal with Level Tracking**

Given a binary tree, perform a level order traversal (breadth-first search).  However, unlike a standard level order traversal, you also need to store and return the level of each node as part of the output.

The output should be a list of tuples, where each tuple contains the node's value and its level in the tree. The root is considered to be at level 0.

**Example:**

```
     1
    / \
   2   3
  / \   \
 4   5   6

Output:  [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2)]
```

**Code Solution (Python):**

```python
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_with_level(root):
    """
    Performs level order traversal of a binary tree, tracking the level of each node.

    Args:
      root: The root node of the binary tree.

    Returns:
      A list of tuples, where each tuple contains (node value, level).
    """

    if not root:
        return []

    result = []
    queue = deque([(root, 0)])  # Queue stores (node, level) tuples

    while queue:
        node, level = queue.popleft()
        result.append((node.val, level))

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return result

# Example usage:
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

traversal_result = level_order_with_level(root)
print(traversal_result)  # Output: [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2)]

# Example with an empty tree
empty_tree_result = level_order_with_level(None)
print(empty_tree_result) # Output: []
```

**Explanation:**

1. **`Node` Class:** Defines the structure of a binary tree node with a value (`val`) and pointers to the left and right children.

2. **`level_order_with_level(root)` Function:**
   - Takes the `root` node of the binary tree as input.
   - Initializes an empty `result` list to store the (value, level) tuples.
   - Creates a `deque` (double-ended queue) called `queue`.  A `deque` is suitable for breadth-first search because it allows efficient appending and popping from both ends.  Initially, it contains the root node and its level (0) as a tuple: `[(root, 0)]`.
   - Enters a `while` loop that continues as long as the `queue` is not empty.
   - Inside the loop:
     - `node, level = queue.popleft()`:  Removes the first element from the `queue` (which is a tuple containing a node and its level) and assigns the values to `node` and `level` respectively.
     - `result.append((node.val, level))`:  Appends a tuple `(node.val, level)` to the `result` list, recording the node's value and its level.
     - `if node.left:`:  If the current node has a left child, it adds the left child and its level (level + 1) to the `queue`.
     - `if node.right:`:  Similarly, if the current node has a right child, it adds the right child and its level (level + 1) to the `queue`.
   - After the `while` loop finishes (when all nodes have been processed), the function returns the `result` list.

**Time and Space Complexity:**

- **Time Complexity:** O(N), where N is the number of nodes in the binary tree.  We visit each node exactly once.
- **Space Complexity:** O(W), where W is the maximum width of the binary tree (i.e., the maximum number of nodes at any level). In the worst-case scenario (a complete binary tree), W is approximately N/2, so the space complexity is effectively O(N). This is due to the `queue` potentially holding all nodes at the widest level of the tree.

**How to Run:**

1.  Save the code as a Python file (e.g., `tree_traversal.py`).
2.  Run it from your terminal: `python tree_traversal.py`

The output will be printed to the console.
