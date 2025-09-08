Okay, here's a problem related to linked lists, a fairly common DSA topic:

**Problem:**

**Reverse Linked List (In-Place)**

Given the head of a singly linked list, reverse the list in-place (without using extra space proportional to the length of the list) and return the new head.

**Example:**

Input: `1 -> 2 -> 3 -> 4 -> 5 -> NULL`
Output: `5 -> 4 -> 3 -> 2 -> 1 -> NULL`

**Constraints:**

*   The number of nodes in the list is in the range `[0, 5000]`.
*   `-5000 <= Node.val <= 5000`

**Python Code Solution:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    """
    Reverses a singly linked list in-place.

    Args:
        head: The head of the linked list.

    Returns:
        The head of the reversed linked list.
    """

    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Store the next node
        curr.next = prev      # Reverse the pointer
        prev = curr           # Move prev to the current node
        curr = next_node      # Move curr to the next node

    return prev  # prev is now the new head
# Example Usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the list
reversed_head = reverseList(head)

# Print the reversed list (for verification)
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

```

**Explanation:**

1.  **`ListNode` Class:**  A simple class to represent a node in the linked list.  It has a `val` (the data) and a `next` pointer to the next node.

2.  **`reverseList(head)` function:**
    *   `prev`:  Keeps track of the previous node in the reversed list.  Initially `None`.
    *   `curr`:  The current node we're processing.  Starts at the head.
    *   `next_node`:  A temporary variable to store the next node in the original list *before* we change the `curr.next` pointer.  This is crucial to not lose the rest of the list.

3.  **`while curr:` loop:**  Iterates through the linked list.
    *   `next_node = curr.next`:  Saves the next node.
    *   `curr.next = prev`:  Reverses the pointer:  The current node's `next` pointer now points to the previous node.
    *   `prev = curr`:  Moves `prev` forward to the current node (which is now part of the reversed portion).
    *   `curr = next_node`:  Moves `curr` to the next node (that we saved earlier).

4.  **`return prev`:**  After the loop finishes, `prev` will be pointing to the new head of the reversed list.

**In-Place:**

The solution is "in-place" because we're only modifying the pointers of the existing nodes. We don't create a new linked list or use extra storage proportional to the size of the input list.  We use a fixed number of extra variables (`prev`, `curr`, `next_node`), so the space complexity is O(1) (constant).

**Time Complexity:**

The algorithm iterates through the linked list once, so the time complexity is O(n), where n is the number of nodes in the list.
