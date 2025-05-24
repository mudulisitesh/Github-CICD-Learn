Okay, here's a DSA problem and a Python solution:

**Problem:**

**Merge K Sorted Linked Lists**

You are given an array of `k` linked-lists, each sorted in ascending order.

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

**Python Code Solution:**

```python
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):  # For heap comparison
        return self.val < other.val


def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of k sorted linked lists.

    Returns:
        The head of the merged sorted linked list.
    """

    heap = []

    # Push the head nodes of all non-empty lists into the heap.
    for head in lists:
        if head:
            heapq.heappush(heap, head)

    # Create a dummy head for the merged list.
    dummy = ListNode()
    tail = dummy

    # While the heap is not empty:
    while heap:
        # Pop the smallest node from the heap.
        node = heapq.heappop(heap)

        # Append the node to the merged list.
        tail.next = node
        tail = tail.next

        # If the popped node has a next node, push it onto the heap.
        if node.next:
            heapq.heappush(heap, node.next)

    # Return the head of the merged list (excluding the dummy node).
    return dummy.next

# Example Usage:
# Create linked lists from the given example
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]

merged_list = mergeKLists(lists)

# Print the merged list (for verification)
def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

print_linked_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

**Explanation:**

1.  **ListNode Class:** Defines the structure of a node in a linked list. It also includes the `__lt__` method which is required to make the ListNode objects comparable in the heap.  This is crucial for using `heapq` correctly when dealing with custom objects.
2.  **Initialization:**
    *   A min-heap `heap` is used to store the head nodes of the input lists.  The min-heap ensures that the node with the smallest value is always at the top.
    *   A dummy node `dummy` is created to simplify the construction of the merged linked list. `tail` points to the last node of the merged list.
3.  **Heap Initialization:** The code iterates through the input `lists`. If a list is not empty (its head is not `None`), the head node is pushed onto the min-heap.
4.  **Merging Process:**
    *   The `while heap:` loop continues as long as there are nodes in the heap.
    *   `heapq.heappop(heap)` retrieves and removes the node with the smallest value from the heap.
    *   The smallest node is appended to the `tail.next` of the merged list. The `tail` is then moved to the newly appended node.
    *   If the popped node has a `next` node, that `next` node is pushed onto the heap to maintain the sorted order.
5.  **Return Value:** After the loop finishes, `dummy.next` points to the head of the merged sorted linked list.

**Time Complexity:** O(N log k), where N is the total number of nodes in all the linked lists, and k is the number of linked lists.  The heap operations (push and pop) take O(log k) time, and we perform these operations N times.

**Space Complexity:** O(k), where k is the number of linked lists. This is the space used by the min-heap. In the worst case, the heap will contain one node from each of the k lists.  The space used by the output linked list is not considered, as it is part of the problem's output requirement.
