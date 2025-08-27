Okay, here's a randomly generated DSA problem and a corresponding Python solution:

**Problem:**

**Reverse a Linked List in Groups of K**

Given the head of a singly linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k`, then left-out nodes in the end should remain as they are.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example:**

Input: `head = [1,2,3,4,5], k = 2`
Output: `[2,1,4,3,5]`

Input: `head = [1,2,3,4,5], k = 3`
Output: `[3,2,1,4,5]`

**Python Code Solution:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    """
    Reverses the linked list in groups of k.

    Args:
        head: The head of the linked list.
        k: The size of the groups to reverse.

    Returns:
        The head of the reversed linked list.
    """

    def reverse_list(head, k):
        """
        Reverses the first k nodes of a linked list.

        Returns:
            A tuple containing the new head and the new tail of the reversed sublist.
        """
        prev, curr = None, head
        count = 0
        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
        return prev, head  # Return the reversed head and the original head (now the tail)

    if not head or k == 1:
        return head

    dummy = ListNode(0)  # Create a dummy node to handle the head case
    dummy.next = head
    group_prev = dummy

    while True:
        # Check if there are k nodes remaining
        kth_node = group_prev
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next  # Not enough nodes for a full group

        # Reverse the current group
        group_next = kth_node.next # save the node after the kth_node
        reversed_head, reversed_tail = reverse_list(group_prev.next, k)

        # Connect the reversed group to the rest of the list
        group_prev.next = reversed_head
        reversed_tail.next = group_next

        # Move to the next group
        group_prev = reversed_tail

    return dummy.next


# Example Usage (with list creation):
def create_linked_list(arr):
    head = None
    tail = None
    for val in arr:
        new_node = ListNode(val)
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def linked_list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

# Example 1:
head1 = create_linked_list([1, 2, 3, 4, 5])
k1 = 2
reversed_head1 = reverse_k_group(head1, k1)
print(linked_list_to_array(reversed_head1))  # Output: [2, 1, 4, 3, 5]


# Example 2:
head2 = create_linked_list([1, 2, 3, 4, 5])
k2 = 3
reversed_head2 = reverse_k_group(head2, k2)
print(linked_list_to_array(reversed_head2))  # Output: [3, 2, 1, 4, 5]

#Example 3 (edge case):
head3 = create_linked_list([1,2,3,4,5])
k3 = 6
reversed_head3 = reverse_k_group(head3, k3)
print(linked_list_to_array(reversed_head3)) #Output: [1, 2, 3, 4, 5]

#Example 4 (k=1):
head4 = create_linked_list([1,2,3])
k4 = 1
reversed_head4 = reverse_k_group(head4, k4)
print(linked_list_to_array(reversed_head4)) #Output: [1, 2, 3]
```

**Explanation:**

1.  **`ListNode` Class:**  Defines the structure of a node in the linked list.

2.  **`reverse_k_group(head, k)` Function:**
    *   Handles the main logic of reversing the linked list in groups of `k`.
    *   Creates a `dummy` node to simplify handling the head of the list.
    *   Iterates through the list, identifying groups of `k` nodes.
    *   Calls the `reverse_list` function to reverse each group.
    *   Connects the reversed groups together.
    *   Returns the new head of the modified linked list (obtained from `dummy.next`).

3.  **`reverse_list(head, k)` Function:**
    *   Reverses a portion of the linked list (up to `k` nodes) using the standard iterative linked list reversal technique.
    *   Returns a tuple: the new head of the reversed sublist, and the original head (which is now the tail).

4.  **`create_linked_list(arr)` Function:** (Helper function)
    *   Creates a linked list from a Python list for easy testing.

5.  **`linked_list_to_array(head)` Function:** (Helper function)
    *   Converts a linked list back into a Python list for easy output and verification.

**How the Algorithm Works:**

*   The `reverse_k_group` function maintains a pointer `group_prev` that points to the node *before* the start of the current group.  This makes connecting the reversed group to the rest of the list easier.
*   For each group, it finds the `kth_node` to determine the end of the group.  If there are fewer than `k` nodes remaining, it means there's an incomplete group at the end, and the function returns.
*   The `reverse_list` function reverses the nodes within the group.
*   Finally, `reverse_k_group` updates the `next` pointers to connect the reversed group into the main list, advancing `group_prev` to the end of the reversed group.

**Time and Space Complexity:**

*   **Time Complexity:** O(N), where N is the number of nodes in the linked list.  Each node is visited and potentially reversed at most once.
*   **Space Complexity:** O(1), as the algorithm uses a constant amount of extra space (excluding the space used for the linked list itself). The reversal is done in-place.

This is a common and important linked list problem.  Understanding how to reverse linked lists in groups is a good skill to have for interviews and problem-solving.
