Okay, here's a DSA problem and a corresponding Python solution.

**Problem:**

**Merge K Sorted Linked Lists**

You are given an array of k linked-lists `lists`, each linked-list is sorted in ascending order.

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

**Code Solution (Python):**

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
        lists: A list of ListNode objects representing the heads of the linked lists.

    Returns:
        A ListNode object representing the head of the merged sorted linked list.
    """

    heap = []  # Min-heap to store nodes from the linked lists
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))  # Store (value, index, node) in the heap

    dummy = ListNode()  # Dummy node to simplify the merging process
    curr = dummy

    while heap:
        val, index, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, index, node.next))  # Push the next node from the same list

    return dummy.next
# Example Usage:
# Create linked lists
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]

# Merge the lists
merged_list = mergeKLists(lists)

# Print the merged list (optional)
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
print(print_linked_list(merged_list)) # Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

**Explanation:**

1. **`ListNode` Class:**  A standard class to represent a node in a linked list.

2. **`mergeKLists(lists)` function:**
   - **Initialization:**
     - `heap = []`: Creates an empty min-heap using `heapq` module.  A min-heap is crucial because it allows us to efficiently retrieve the smallest element across all k lists at any given time.
     - `dummy = ListNode()`: Creates a dummy node. This is a common technique in linked list problems to simplify the handling of the head of the new merged list. We'll point `curr` to this dummy, and then `dummy.next` will eventually be the actual merged list.
     - **Populating the Heap:** The code iterates through the input `lists`. For each linked list, if it's not empty (`if head:`), it pushes the first node's value along with its index in the `lists` and the node itself onto the heap. `heapq.heappush` maintains the heap property (min-heap).  The index is added to the tuple so that if two values are equal, the tie is broken using the original list index.

   - **Merging:**
     - `while heap:`:  The loop continues as long as there are elements in the heap (i.e., nodes to be processed).
     - `val, index, node = heapq.heappop(heap)`: Extracts the node with the smallest value from the heap. The `heapq.heappop` function returns the smallest element and removes it from the heap.
     - `curr.next = node`: Connects the current node (`curr`) of the merged list to the extracted node (`node`).
     - `curr = curr.next`: Moves `curr` to the newly added node, preparing for the next insertion.
     - `if node.next:`:  Checks if the extracted node has a next node in its original list. If it does, the next node (along with its value and original list index) is pushed onto the heap.

   - **Return:** `return dummy.next`:  Finally, the function returns the `next` pointer of the dummy node, which is the head of the merged sorted linked list.

**Time and Space Complexity:**

*   **Time Complexity:** O(N log k), where N is the total number of nodes across all k lists, and k is the number of lists.  `heapq.heappush` and `heapq.heappop` take O(log k) time, and we perform these operations for each of the N nodes.
*   **Space Complexity:** O(k), where k is the number of linked lists. This is the space used by the min-heap.  In the worst case (all nodes are very small), we might have k elements in the heap simultaneously.  The output list takes O(N) space, but it is part of the output, so it's typically not counted towards the auxiliary space complexity of the algorithm.
