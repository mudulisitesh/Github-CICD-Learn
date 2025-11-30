Okay, here's a random DSA problem and a Python solution:

**Problem:**

**Kth Largest Element in an Array**

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

**Example:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints:**

*   `1 <= k <= nums.length <= 10^5`
*   `-10^4 <= nums[i] <= 10^4`

**Python Solution (using `heapq` module - min-heap):**

```python
import heapq

def findKthLargest(nums, k):
    """
    Finds the kth largest element in an array.

    Args:
        nums: The input array of integers.
        k: The k-th largest element to find (1-indexed).

    Returns:
        The kth largest element in the array.
    """
    return heapq.nlargest(k, nums)[-1]

# Example Usage:
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"Kth largest element in {nums1} for k={k1}: {findKthLargest(nums1, k1)}")  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(f"Kth largest element in {nums2} for k={k2}: {findKthLargest(nums2, k2)}")  # Output: 4

nums3 = [1]
k3 = 1
print(f"Kth largest element in {nums3} for k={k3}: {findKthLargest(nums3, k3)}")
```

**Explanation:**

1.  **`heapq` module (Min-Heap):** The Python `heapq` module provides an implementation of the heap queue algorithm (also known as the priority queue algorithm).  By default, it implements a min-heap.

2.  **`heapq.nlargest(k, nums)`:** This function efficiently finds the *k* largest elements from the input list `nums` and returns them as a new list. Because we only care about the *k*-th largest (not necessarily all the *k* largest), this avoids unnecessary heap operations if *k* is relatively small compared to the length of `nums`. We retrieve the last element of this list using `[-1]`, which will be the *k*-th largest element.

**Time and Space Complexity:**

*   **Time Complexity:** O(N log k), where N is the length of the `nums` array.  `heapq.nlargest` has a time complexity of `O(n log k)` in the worst case because it builds a min-heap of size `k` and then iterates through the remaining elements in `nums`.

*   **Space Complexity:** O(k), as it uses a min-heap of size `k` to store the *k* largest elements seen so far.

**Alternative solution (using quickselect - average O(N)):**

While the solution above is often preferred due to its clarity and use of built-in functions, here's a potentially faster (in the *average* case) solution using the Quickselect algorithm.  Quickselect is a selection algorithm related to Quicksort.  Its advantage is that, on average, it has a linear time complexity O(N).  However, its worst-case time complexity is O(N^2).

```python
import random

def findKthLargest_quickselect(nums, k):
    """
    Finds the kth largest element in an array using Quickselect.

    Args:
        nums: The input array of integers.
        k: The k-th largest element to find (1-indexed).

    Returns:
        The kth largest element in the array.
    """

    def partition(l, r):
        pivot = nums[r]  # Choose the last element as pivot
        i = l - 1

        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]  # Swap

        nums[i + 1], nums[r] = nums[r], nums[i + 1]  # Place pivot in correct position
        return i + 1

    def quickselect(l, r, target):
        if l == r:
            return nums[l]

        pivot_index = partition(l, r)

        if target == pivot_index:
            return nums[target]
        elif target < pivot_index:
            return quickselect(l, pivot_index - 1, target)
        else:
            return quickselect(pivot_index + 1, r, target)

    n = len(nums)
    target_index = n - k  # Convert kth largest to index from smallest
    return quickselect(0, n - 1, target_index)


# Example usage:
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"Kth largest element in {nums1} for k={k1}: {findKthLargest_quickselect(nums1, k1)}")  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(f"Kth largest element in {nums2} for k={k2}: {findKthLargest_quickselect(nums2, k2)}")  # Output: 4

nums3 = [1]
k3 = 1
print(f"Kth largest element in {nums3} for k={k3}: {findKthLargest_quickselect(nums3, k3)}")
```

**Explanation of Quickselect:**

1.  **`partition(l, r)`:** This function partitions the sub-array `nums[l:r+1]` around a pivot element (chosen as the last element in this implementation).  It rearranges the elements such that all elements less than or equal to the pivot are placed before it, and all elements greater than the pivot are placed after it.  It returns the index of the pivot after partitioning.

2.  **`quickselect(l, r, target)`:** This function recursively selects the element at the `target` index (which corresponds to the (n-k)th smallest element, i.e., the kth largest).

    *   If `l == r`, it means we've reached a sub-array of size 1, so we return the element at that index.
    *   It partitions the sub-array and gets the index of the pivot (`pivot_index`).
    *   If `target == pivot_index`, we've found the element we're looking for, so we return it.
    *   If `target < pivot_index`, it means the target element is in the left sub-array, so we recursively call `quickselect` on the left sub-array.
    *   If `target > pivot_index`, it means the target element is in the right sub-array, so we recursively call `quickselect` on the right sub-array.

3.  **Main Logic:** The main `findKthLargest_quickselect` function converts the `k`th largest problem into finding the `(n - k)`th smallest element (where `n` is the length of `nums`) and then calls the `quickselect` function.

**Time and Space Complexity of Quickselect:**

*   **Time Complexity:**
    *   **Average:** O(N) - On average, Quickselect has a linear time complexity.
    *   **Worst:** O(N^2) - The worst case occurs when the pivot is consistently the smallest or largest element, leading to unbalanced partitions.
*   **Space Complexity:** O(1) - Quickselect is an in-place algorithm, meaning it doesn't require significant extra space (beyond the call stack for recursion). The recursion depth can be at most `N` in the worst case (O(N)), but on average, it's much less.

**Choice of Solution:**

*   If you prioritize simplicity and readability, the `heapq.nlargest` solution is often preferred, especially if `k` is relatively small compared to the size of `nums`.

*   If performance is paramount and you want to try to optimize for the average case, `quickselect` can be a good option.  However, be aware of its potential O(N^2) worst-case behavior.  You could further mitigate this by using a randomized pivot selection strategy (e.g., swapping the last element with a randomly chosen element before partitioning) to reduce the probability of consistently encountering bad pivots.
