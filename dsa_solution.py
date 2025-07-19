Okay, here's a DSA problem focusing on linked lists, along with a Python solution:

**Problem:**

**Reverse Nodes in k-Group**

Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k`, then left-out nodes, in the end, should remain as they are.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example:**

*   **Input:** `head = [1,2,3,4,5], k = 2`
*   **Output:** `[2,1,4,3,5]`

*   **Input:** `head = [1,2,3,4,5], k = 3`
*   **Output:** `[3,2,1,4,5]`

**Constraints:**

*   The number of nodes in the list is `n`.
*   `1 <= k <= n <= 5000`
*   `0 <= Node.val <= 1000`

**Python Solution:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    """
    Reverses the linked list in groups of k nodes.

    Args:
        head: The head of the linked list.
        k: The size of each group to reverse.

    Returns:
        The head of the modified linked list.
    """

    def reverseList(start, end):
        """Reverses a portion of the linked list."""
        prev = None
        curr = start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def get_kth_node(head, k):
        """Finds the kth node from head, return None if there is no kth node."""
        curr = head
        for _ in range(k - 1): # Stop at the (k-1)th node, since we need to point to the kth.
            if not curr:
                return None
            curr = curr.next
        return curr

    if not head or k <= 1:
        return head

    dummy = ListNode(0)  # Dummy node to handle the case where the head needs to be changed
    dummy.next = head
    group_prev = dummy

    while True:
        kth_node = get_kth_node(group_prev.next, k)
        if not kth_node: #Not enough nodes remaining, so don't reverse
            break

        group_next = kth_node.next # Node after group

        reversed_head = reverseList(group_prev.next, group_next)

        # Connect the reversed group to the rest of the list
        group_next_to_reverse = group_prev.next
        group_prev.next = reversed_head
        group_next_to_reverse.next = group_next

        group_prev = group_next_to_reverse # Update to beginning of next possible group
    return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to convert a linked list to a list of values (for testing)
def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# Example usage:
if __name__ == '__main__':
    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    k1 = 2
    reversed_head1 = reverseKGroup(head1, k1)
    print(f"Input: [1,2,3,4,5], k={k1}, Output: {linked_list_to_list(reversed_head1)}")  # Output: [2, 1, 4, 3, 5]

    # Test case 2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    k2 = 3
    reversed_head2 = reverseKGroup(head2, k2)
    print(f"Input: [1,2,3,4,5], k={k2}, Output: {linked_list_to_list(reversed_head2)}") # Output: [3, 2, 1, 4, 5]

    # Test case 3
    head3 = create_linked_list([1, 2, 3, 4, 5])
    k3 = 1
    reversed_head3 = reverseKGroup(head3, k3)
    print(f"Input: [1,2,3,4,5], k={k3}, Output: {linked_list_to_list(reversed_head3)}") # Output: [1, 2, 3, 4, 5]

    # Test case 4
    head4 = create_linked_list([1, 2])
    k4 = 2
    reversed_head4 = reverseKGroup(head4, k4)
    print(f"Input: [1,2], k={k4}, Output: {linked_list_to_list(reversed_head4)}") # Output: [2, 1]

    # Test case 5
    head5 = create_linked_list([1])
    k5 = 2  # k > n, should return original
    reversed_head5 = reverseKGroup(head5, k5)
    print(f"Input: [1], k={k5}, Output: {linked_list_to_list(reversed_head5)}") # Output: [1]

    # Test case 6
    head6 = create_linked_list([])
    k6 = 2  # empty list case
    reversed_head6 = reverseKGroup(head6, k6)
    print(f"Input: [], k={k6}, Output: {linked_list_to_list(reversed_head6)}") # Output: []
```

**Explanation:**

1.  **`ListNode` Class:** Defines the structure of a node in the linked list (value and pointer to the next node).

2.  **`reverseKGroup(head, k)` Function:**
    *   **Base Cases:**  If the list is empty (`not head`) or `k` is less than or equal to 1, there's nothing to reverse, so return the original list.
    *   **Dummy Node:** Create a dummy node (`dummy`) that points to the head of the list.  This simplifies the code, especially when the head of the list needs to be changed.
    *   **`group_prev` Pointer:**  Initialize a pointer `group_prev` to the dummy node. This pointer will keep track of the node *before* the group that needs to be reversed.
    *   **Main Loop:** The `while True` loop iterates as long as there are enough nodes remaining to form a group of `k` nodes.
        *   **`get_kth_node(head, k)` Function:** This helper function finds the kth node from the starting node. If there aren't `k` nodes available, it returns `None`.
        *   **Check for Enough Nodes:** `if not kth_node:` If `get_kth_node` returns `None`, it means there are fewer than `k` nodes left.  In this case, we break out of the loop because we don't reverse the remaining nodes.
        *   **`group_next` Pointer:** Store a pointer to the node *after* the `k`th node.  This is important for connecting the reversed group to the rest of the list.
        *   **`reverseList(start, end)` Function:** This is the core part. It reverses the portion of the linked list starting from `group_prev.next` up to (but not including) `group_next`.  It returns the new head of the reversed portion (which was the original `k`th node).
        *   **Connecting the Reversed Group:** After reversing:
            *   `group_next_to_reverse = group_prev.next` stores a temporary reference to the *original* head of the `k` node group.
            *   `group_prev.next = reversed_head` connects the previous group (or the dummy node) to the new head of the reversed group.
            *   `group_next_to_reverse.next = group_next` connects the end of the reversed group (which was the original head) to the node following the group.
        *   **Update `group_prev`:** Move `group_prev` to `group_next_to_reverse`, which is now the node before the next potential group to reverse.
    *   **Return the New Head:**  Finally, return `dummy.next`, which is the head of the modified list.

3.  **`reverseList(start, end)` Function:**
    *   This function reverses a portion of the linked list between `start` (inclusive) and `end` (exclusive). It's a standard linked list reversal algorithm.

4.  **`get_kth_node(head, k)` Function:**
    *   A helper function to find the kth node in a linked list.

5.  **`create_linked_list` and `linked_list_to_list`:** These are helper functions to make testing easier.  They create a linked list from a Python list and convert a linked list back to a Python list, respectively.

**Key Concepts Used:**

*   **Linked Lists:**  The problem revolves around manipulating linked list nodes.
*   **Iteration:**  Iterating through the linked list to find groups of `k` nodes.
*   **Reversal:**  Reversing a portion of the linked list.
*   **Pointers:**  Using pointers (`prev`, `curr`, `next_node`, `group_prev`, `group_next`) to keep track of the nodes and manipulate the list.
*   **Dummy Node:** A common technique in linked list problems to simplify edge cases (e.g., when the head of the list needs to be modified).

**How to Run the Code:**

1.  Copy and paste the entire code (including the `ListNode` class and the helper functions) into a Python environment (e.g., a Python interpreter, a Jupyter notebook, or a Python script file).
2.  Run the script. The example usage at the end will create linked lists, reverse them in groups of `k`, and print the results.  You can modify the input lists and values of `k` to test the code with different scenarios.
