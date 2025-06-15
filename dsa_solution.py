Okay, here's a DSA problem and a Python solution:

**Problem:  Merge K Sorted Lists**

You are given an array of `k` linked lists, each linked list is sorted in ascending order.

Merge all the linked lists into one sorted linked list and return it.

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

**Solution (Python):**

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
        lists: A list of ListNode heads of the k sorted linked lists.

    Returns:
        The head of the merged sorted linked list.
    """

    heap = []  # Min-heap to store nodes based on their values.
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head)) # (value, list_index, node)
            # list_index used to break ties in case of equal values.  Crucial for correct heapq operation.

    dummy = ListNode()  # Dummy node to start the merged list.
    current = dummy

    while heap:
        val, list_index, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, list_index, node.next))

    return dummy.next


# Example Usage:
def create_linked_list(arr):
    """Creates a linked list from a Python list."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def linked_list_to_list(head):
    """Converts a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example Input
list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])

lists = [list1, list2, list3]

# Merge the lists
merged_list_head = mergeKLists(lists)

# Convert the merged list to a Python list for easy printing
merged_list = linked_list_to_list(merged_list_head)

print(merged_list) # Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

**Explanation:**

1. **`ListNode` Class:** Defines the structure of a node in the linked list.

2. **`mergeKLists(lists)` Function:**
   - Takes a list of linked list heads (`lists`) as input.
   - **Min-Heap:**  Uses a `heapq` (min-heap) to efficiently keep track of the smallest node value among all the lists.  We store tuples of `(value, list_index, node)` in the heap.
     - The `list_index` is *crucial* for proper heap behavior when values are the same.  `heapq` needs a consistent tie-breaker. Without it, if two nodes from different lists have the same value, the heap can become corrupted leading to incorrect merging.
   - **Initialization:**
     - Iterates through the input `lists`.
     - If a list is not empty (i.e., `head` is not `None`), the head node's value and the node itself are pushed onto the heap.  We also push the list index.
   - **Merging:**
     - A `dummy` node is created to simplify the merging process (avoids special handling for the first node).
     - `current` pointer tracks the current node in the merged list.
     - While the heap is not empty:
       - The node with the smallest value (`val`) is popped from the heap.
       - The node is appended to the merged list (`current.next = node`).
       - `current` is moved to the newly added node (`current = current.next`).
       - If the popped node has a `next` node, that `next` node's value and node are pushed onto the heap (along with the list index from which it came).
   - **Return:**  Returns the `next` of the `dummy` node, which is the head of the merged sorted linked list.

3. **Helper Functions (for Example):**
   - `create_linked_list(arr)`: Creates a linked list from a Python list.  This is used to set up the input.
   - `linked_list_to_list(head)`: Converts a linked list back to a Python list, so we can easily print and verify the output.

**Time Complexity:**

*   O(N log k), where N is the total number of nodes in all the linked lists, and k is the number of linked lists.  Each node is added to and removed from the heap once.  Heap operations take O(log k) time.

**Space Complexity:**

*   O(k): The space complexity is dominated by the heap, which stores at most one node from each of the k linked lists at any given time.
