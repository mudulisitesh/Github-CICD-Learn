Okay, here's a DSA problem and a working Python solution, designed to be a reasonably common and useful type:

**Problem:**

**Merge K Sorted Lists**

You are given an array of `k` linked-lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Constraints:**

*   `k == len(lists)`
*   `0 <= k <= 10^4`
*   `0 <= lists[i].length <= 500`
*   `-10^4 <= lists[i][j] <= 10^4`
*   `lists[i]` is sorted in ascending order.
*   The sum of `lists[i].length` will not exceed `10^4`.

**Python Solution (using a Heap/Priority Queue):**

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
        lists: A list of ListNode objects, where each ListNode represents the head
               of a sorted linked list.

    Returns:
        A ListNode object representing the head of the merged sorted linked list.
    """

    heap = []  # Priority queue (min-heap) to store the heads of the lists.
    # Initialize the heap with the heads of the non-empty lists.
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i])) # (val, index, node) to handle equal vals

    # Create a dummy node to start the merged list.
    dummy = ListNode()
    tail = dummy

    while heap:
        val, index, node = heapq.heappop(heap)

        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(heap, (node.next.val, index, node.next))

    return dummy.next

# Example Usage (with example input as linked lists):
def create_linked_list(arr):
    """Helper function to create a linked list from a list."""
    dummy = ListNode()
    tail = dummy
    for val in arr:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

# Example usage:
lists = [create_linked_list([1,4,5]), create_linked_list([1,3,4]), create_linked_list([2,6])]

merged_list = mergeKLists(lists)

# Function to print a linked list for verification:
def print_linked_list(head):
    """Helper function to print a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

print_linked_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

**Explanation:**

1.  **ListNode Class:** Defines a simple linked list node structure.

2.  **`mergeKLists(lists)` Function:**
    *   **Heap Initialization:**  A `heap` (implemented using Python's `heapq`) is used as a priority queue.  We store tuples of `(value, index, node)` in the heap. `value` is used for sorting by value in the heap. `index` is used to distinguish between different nodes that have the same value.  `node` is the actual `ListNode` object. This ensures we can push linked list heads into the heap based on their values. We only push non-empty linked lists.
    *   **Dummy Node:** A `dummy` node is created to simplify the construction of the merged list.  `tail` points to the last node added to the merged list so far.
    *   **Heap Processing:**  The `while heap` loop continues as long as there are nodes in the heap.
        *   `heapq.heappop(heap)`: Removes the node with the smallest value from the heap.
        *   The extracted node is appended to the merged list (via `tail.next`).
        *   If the extracted node has a `next` node, that `next` node is added to the heap.
    *   **Return:** Returns `dummy.next`, which is the head of the merged sorted list.

3.  **Helper Functions:**
    *   `create_linked_list(arr)`:  A helper function to create a linked list from a Python list, useful for creating the example input.
    *   `print_linked_list(head)`: A helper function to print the content of a linked list so you can verify the output.

**Time Complexity:** O(N log k), where N is the total number of nodes in all the linked lists, and k is the number of linked lists.  Each node is added to and removed from the heap once. The heap operations (push and pop) take O(log k) time.

**Space Complexity:** O(k), where k is the number of linked lists.  This is the space used by the heap to store the heads of the linked lists.  The merged linked list itself takes O(N) space. In the worst case, if all lists have elements, the space complexity of the heap will be O(k).
