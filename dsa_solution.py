Okay, here's a problem related to **Binary Trees** and a Python solution:

**Problem:**

Given a binary tree where each node contains an integer value, find the maximum sum of any path from root to a leaf node.

**Example:**

```
     4
    / \
   2   7
  / \   \
 1   3   9

```

In the above tree, the maximum root-to-leaf path sum is 4 + 7 + 9 = 20.

**Python Code Solution:**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_root_to_leaf_sum(root):
    """
    Finds the maximum sum of a path from root to a leaf node in a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The maximum root-to-leaf path sum.
    """

    if not root:
        return 0

    if not root.left and not root.right:  # It's a leaf node
        return root.val

    left_sum = max_root_to_leaf_sum(root.left) if root.left else float('-inf')
    right_sum = max_root_to_leaf_sum(root.right) if root.right else float('-inf')

    return root.val + max(left_sum, right_sum)

# Example usage (creating the tree from the problem description)
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

max_sum = max_root_to_leaf_sum(root)
print(f"Maximum root-to-leaf path sum: {max_sum}")  # Output: 20
```

**Explanation:**

1. **`TreeNode` Class:** Defines the structure of a node in a binary tree.  Each node has a value (`val`), a left child (`left`), and a right child (`right`).

2. **`max_root_to_leaf_sum(root)` Function:**
   - **Base Cases:**
     - `if not root: return 0`:  If the tree is empty (no root), the sum is 0.
     - `if not root.left and not root.right: return root.val`: If it's a leaf node (no left or right child), the maximum sum is just the node's value.

   - **Recursive Step:**
     - `left_sum = max_root_to_leaf_sum(root.left) if root.left else float('-inf')`:  Recursively calculates the maximum path sum from the *left* subtree.  If there is no left subtree it will be negative infinity.
     - `right_sum = max_root_to_leaf_sum(root.right) if root.right else float('-inf')`: Recursively calculates the maximum path sum from the *right* subtree. If there is no right subtree it will be negative infinity.
     - `return root.val + max(left_sum, right_sum)`:  Adds the current node's value to the maximum of the left and right subtree sums, and returns the result. This represents the maximum path sum from the current node to a leaf node. We take the max of left_sum and right_sum because we want the *longest* path.  We need to find the max from one side otherwise the path won't be from root to leaf.

3. **Example Usage:**
   - Creates the example binary tree as described in the problem statement.
   - Calls `max_root_to_leaf_sum(root)` to get the maximum path sum.
   - Prints the result.

**How it works:**

The code uses a recursive approach.  It traverses the tree in a depth-first manner.  For each node, it recursively calculates the maximum path sum from its left and right subtrees. Then, it adds the node's value to the larger of the two subtree sums to get the maximum path sum from that node. The base cases handle the conditions when the tree is empty or when a leaf node is reached.
The negative infinity check prevents null paths from being favored over other possible paths.
**Time and Space Complexity:**

- **Time Complexity:** O(N), where N is the number of nodes in the binary tree.  The function visits each node once.
- **Space Complexity:** O(H), where H is the height of the binary tree. This is due to the call stack during recursion. In the worst case (a skewed tree), H can be equal to N, leading to O(N) space complexity. In the best case (a balanced tree), H would be log(N), resulting in O(log N) space complexity.
