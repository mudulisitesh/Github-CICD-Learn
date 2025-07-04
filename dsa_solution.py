Okay, here's a randomly generated DSA problem and a Python solution:

**Problem:**

**K-th Largest Element in a Stream**

Design a class to find the k-th largest element in a stream.  You will be given an integer `k` and an initial array of integers `nums`. Your class should have the following methods:

*   `__init__(self, k: int, nums: List[int])`: Initializes the object with the integer `k` and the stream of integers `nums`.
*   `add(self, val: int) -> int`: Appends the integer `val` to the stream and returns the k-th largest element in the current stream.  If the stream has fewer than `k` elements, return the smallest element.

**Example:**

```python
k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(3, nums)
print(kthLargest.add(3))   # Output: 4
print(kthLargest.add(5))   # Output: 5
print(kthLargest.add(10))  # Output: 5
print(kthLargest.add(9))   # Output: 8
print(kthLargest.add(4))   # Output: 8
```

**Python Solution:**

```python
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums  # initialize heap with initial nums
        heapq.heapify(self.heap)

        # maintain only the k largest elements in the heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # maintain only the k largest elements in the heap
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0] # the root of the heap is the kth largest


# Example Usage:
k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums)
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
```

**Explanation:**

1.  **`__init__(self, k: int, nums: List[int])`:**
    *   Stores `k`.
    *   Initializes a min-heap (`self.heap`) with the initial `nums`. A min-heap is used because we want to quickly access and remove the *smallest* element among the largest `k` elements.
    *   `heapq.heapify(self.heap)` converts the list `self.heap` into a heap in-place.
    *   The `while` loop ensures that the heap only contains the `k` largest elements from the initial list.  It repeatedly removes the smallest element (root of the min-heap) until the heap size is `k`.

2.  **`add(self, val: int) -> int`:**
    *   `heapq.heappush(self.heap, val)` adds the new value `val` to the heap.  The heap property is maintained after the insertion.
    *   If the heap's size becomes greater than `k`, we remove the smallest element using `heapq.heappop(self.heap)`. This ensures that `self.heap` always contains the `k` largest elements seen so far.
    *   The root of the min-heap, `self.heap[0]`, is now the k-th largest element in the stream, so we return it.

**Why this is efficient:**

*   **Heap Data Structure:**  Using a min-heap is crucial.  Finding the smallest of `k` elements in a heap takes O(1) time.  Adding or removing an element from a heap takes O(log k) time, where `k` is the number of elements in the heap.
*   **Time Complexity:**
    *   `__init__`: O(n log k), where n is the length of the initial `nums` array.  Heapifying takes O(n), and then the while loop takes at most O(n log k) (actually better in practice).
    *   `add`: O(log k) because we do a `heappush` and a possible `heappop`.
*   **Space Complexity:** O(k), as we only store `k` elements in the heap.

**Alternative (but less efficient for streams with a lot of `add` calls):**

A simpler, but potentially less efficient, approach would be to simply sort the list in the `add` function each time and return the k-th largest element. This would have a time complexity of O(n log n) for each `add` call, where n is the current number of elements in the stream. The heap-based approach is much better when you need to call `add` many times.
