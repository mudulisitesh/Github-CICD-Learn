Okay, here's a DSA problem with a Python solution:

**Problem:**

**Merge K Sorted Lists**

You are given an array of k linked-lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation:
The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Constraints:**

*   `k == lists.length`
*   `0 <= k <= 10^4`
*   `0 <= lists[i].length <= 500`
*   `-10^4 <= lists[i][j] <= 10^4`
*   `lists[i]` is sorted in ascending order.
*   The sum of `lists[i].length` will not exceed `10^4`.

**Python Solution (using a min-heap):**

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
      lists: A list of k sorted linked lists.

    Returns:
      The head of the merged sorted linked list.
    """

    heap = []
    # Add the head of each list to the heap.  Use index as tie breaker for lists with same head value.
    for i in range(len(lists)):
        if lists[i]:  # Ensure list is not empty
            heapq.heappush(heap, (lists[i].val, i, lists[i]))  # (value, index, node)

    dummy = ListNode()  # Dummy node for the merged list
    curr = dummy

    while heap:
        val, index, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, index, node.next))  # (value, index, node)

    return dummy.next

# Example Usage (for testing):

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

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]

merged_list_head = mergeKLists(lists)
merged_list = linked_list_to_list(merged_list_head)  # Convert to a regular list for easy printing
print(merged_list)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]

lists2 = [
    create_linked_list([]),
    create_linked_list([])
]

merged_list_head2 = mergeKLists(lists2)
merged_list2 = linked_list_to_list(merged_list_head2)  # Convert to a regular list for easy printing
print(merged_list2)  # Output: []

lists3 = [create_linked_list([])]
merged_list_head3 = mergeKLists(lists3)
merged_list3 = linked_list_to_list(merged_list_head3)  # Convert to a regular list for easy printing
print(merged_list3) # Output: []
```

Key improvements and explanations:

*   **`ListNode` class:**  Includes the standard `ListNode` definition for a linked list node.  This is essential for working with linked lists.
*   **Heap-based Solution:** The solution uses a min-heap (priority queue) to efficiently find the smallest element among all the lists at each step.
*   **Correct Heap Ordering:** Critically, the `heapq.heappush()` calls now store a tuple `(lists[i].val, i, lists[i])`.  This ensures correct ordering in the heap *and* allows us to keep track of which list the node came from using the `i` (index). The index serves as a tie-breaker in case of duplicate values in different lists, preventing potential comparison errors.
*   **Empty List Handling:** The code explicitly checks `if lists[i]:` before adding a linked list to the heap. This correctly handles cases where some of the input lists are empty, preventing `AttributeError` exceptions.
*   **Dummy Node:** Uses a `dummy` node to simplify the construction of the merged linked list.  This avoids special cases for the head of the merged list.
*   **Clearer Variable Names:**  `curr` instead of just `p` for the current node in the merged list.
*   **Complete and runnable example:**  Includes example usage with a `create_linked_list` helper function to easily create test linked lists from Python lists and `linked_list_to_list` to convert the merged list back to a standard list for printing and validation.  This makes the code fully self-contained and testable.  More test cases added, including empty lists.
*   **Comments:** More detailed comments explaining each step of the algorithm.
*   **Type Hints (optional):**  You could add type hints for even better readability and maintainability:

```python
from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
      lists: A list of k sorted linked lists.

    Returns:
      The head of the merged sorted linked list.
    """
    # ... (rest of the code remains the same)

```

**Explanation:**

1.  **`ListNode` Class:** Defines the node structure for the linked list.

2.  **`mergeKLists(lists)` Function:**
    *   `heap`: A min-heap to store the head nodes of the linked lists. We store a tuple: `(node.val, index_of_list, node)` so that we can use the value to compare them and the index to differentiate nodes with equal values (avoids comparing nodes directly, which can cause errors).
    *   We iterate through the input `lists` and add the head node of each non-empty list to the heap.
    *   `dummy`:  A dummy node is created to simplify the construction of the merged linked list.
    *   `curr`:  A pointer to the current node in the merged list.
    *   **`while heap:` loop:**
        *   `heapq.heappop(heap)`: Retrieves the node with the smallest value from the heap (the `val` in the tuple).  The `index` is used to identify the list that the node came from.
        *   `curr.next = node`: Appends the smallest node to the merged list.
        *   `curr = curr.next`: Moves the `curr` pointer to the newly added node.
        *   If the retrieved node has a `next` node, add that `next` node to the heap.  This keeps the heap populated with the next candidate nodes to be added to the merged list.
    *   `return dummy.next`: Returns the head of the merged list (skipping the dummy node).

**Time Complexity:** O(N log k), where N is the total number of nodes in all the linked lists and k is the number of linked lists. Each node is added to and removed from the heap once.  Heap operations (insertion and deletion) take O(log k) time.

**Space Complexity:** O(k), where k is the number of linked lists.  The heap stores at most k nodes (one from each list).  O(1) excluding the space occupied by the output.
