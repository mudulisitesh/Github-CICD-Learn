Okay, here's a DSA problem and its Python solution:

**Problem:**

**Merge K Sorted Lists**

You are given an array of `k` linked-lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

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

*   `k == lists.length`
*   `0 <= k <= 10^4`
*   `0 <= lists[i].length <= 500`
*   `-10^4 <= lists[i][j] <= 10^4`
*   `lists[i]` is sorted in ascending order.
*   The sum of `lists[i].length` will not exceed `10^4`.

**Python Solution:**

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
        lists: A list of ListNode objects representing the heads of the k sorted lists.

    Returns:
        A ListNode object representing the head of the merged sorted list.
    """

    heap = []  # Min-heap to store the smallest nodes from each list
    for i in range(len(lists)):
        if lists[i]: #Only push into heap if the list is not empty
            heapq.heappush(heap, (lists[i].val, i, lists[i])) #Push (val, index, node)

    dummy = ListNode(0)  # Dummy node for the merged list
    curr = dummy

    while heap:
        val, index, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, index, node.next))

    return dummy.next

# Example Usage (for testing)

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next
    return head

# Helper function to convert a linked list to a list for easy comparison
def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# Example lists
list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])

lists = [list1, list2, list3]

# Merge the lists
merged_list = mergeKLists(lists)

# Convert the merged list to a list for output
merged_list_values = linked_list_to_list(merged_list)

print(merged_list_values)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]

list4 = create_linked_list([])
list5 = create_linked_list([1,2,3])
lists = [list4, list5]

merged_list = mergeKLists(lists)
merged_list_values = linked_list_to_list(merged_list)

print(merged_list_values) #Output: [1, 2, 3]
```

**Explanation:**

1.  **`ListNode` Class:** Defines the structure of a node in a linked list.

2.  **`mergeKLists(lists)` Function:**
    *   **Heap:**  Uses a min-heap (`heapq`) to keep track of the smallest node from each list. The heap stores tuples of `(node.val, index, node)` where index is the list index, this makes sure when the values are equal, the heap doesn't compare the nodes, which aren't comparable and throw an error.
    *   **Initialization:**
        *   Iterates through the input `lists`.
        *   For each non-empty list, it pushes the first node (value and the list index) onto the heap.
        *   Creates a dummy node `dummy` to simplify the construction of the merged list.  `curr` pointer is initialized to `dummy`.
    *   **Merging Process:**
        *   While the heap is not empty:
            *   `heapq.heappop(heap)` removes the smallest node (along with the list index and node itself) from the heap.
            *   Appends this node to the merged list by `curr.next = node`.  Moves `curr` forward: `curr = curr.next`.
            *   If the removed node has a `next` node, pushes the `next` node (along with the list index) onto the heap.
    *   **Return:** Returns `dummy.next`, which is the head of the merged sorted linked list.

3.  **Helper Functions (for testing):**
    *   `create_linked_list(values)`: Creates a linked list from a list of values.
    *   `linked_list_to_list(head)`: Converts a linked list to a regular Python list (for easy printing and comparison).

**Key Concepts:**

*   **Min-Heap:**  The min-heap efficiently finds the smallest element among the heads of the `k` lists at any given time.  `heapq` in Python provides a min-heap implementation.
*   **Linked Lists:**  Understanding how to manipulate linked list nodes (creating, traversing, appending) is crucial.
*   **Dummy Node:** The dummy node simplifies the process of building the merged list, especially when handling the head node.
*   **Time Complexity:** O(N log k), where N is the total number of nodes across all lists and k is the number of lists.  Each node is added to the heap and removed once. The heap operations (push and pop) take O(log k) time.
*   **Space Complexity:** O(k) due to the size of the min-heap, which at most contains one node from each of the `k` lists. O(1) additional space if you don't consider the space for the resulting linked list.
