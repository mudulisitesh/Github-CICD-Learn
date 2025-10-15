Okay, here's a randomly generated DSA problem and a Python solution:

**Problem:**

**Implement a function `kth_largest(nums, k)` that finds the k-th largest element in an unsorted array `nums`.  You cannot use any built-in sorting functions (like `nums.sort()`). You need to implement it yourself.  Assume `1 <= k <= len(nums)`.**

**Example:**

```
nums = [3, 2, 1, 5, 6, 4]
k = 2
kth_largest(nums, k) == 5  # The 2nd largest element is 5.

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
kth_largest(nums, k) == 4  # The 4th largest element is 4.
```

**Python Solution (using QuickSelect Algorithm):**

```python
import random

def kth_largest(nums, k):
    """
    Finds the k-th largest element in an unsorted array.

    Args:
        nums: The list of integers.
        k: The k-th largest element to find (1-indexed).

    Returns:
        The k-th largest element in the array.
    """

    def partition(l, r):
        """Partitions the array around a pivot."""
        pivot = nums[r]  # Choose the last element as the pivot
        i = l - 1  # Index of smaller element

        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]  # Swap if element is smaller than pivot

        nums[i + 1], nums[r] = nums[r], nums[i + 1]  # Place pivot in its correct position
        return i + 1

    def quickselect(l, r, k):
        """Recursively finds the k-th largest element using QuickSelect."""
        if l == r:
            return nums[l]

        pivot_index = partition(l, r)

        if k == pivot_index + 1:  # k-th element from start
            return nums[pivot_index]
        elif k < pivot_index + 1:
            return quickselect(l, pivot_index - 1, k)
        else:
            return quickselect(pivot_index + 1, r, k)

    # Convert k to find the k-th smallest from the end.
    n = len(nums)
    k_smallest_from_start = n - k + 1
    return quickselect(0, n - 1, k_smallest_from_start)


# Example Usage:
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"The {k1}th largest element in {nums1} is: {kth_largest(nums1, k1)}")  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(f"The {k2}th largest element in {nums2} is: {kth_largest(nums2, k2)}")  # Output: 4

nums3 = [7,6,5,4,3,2,1]
k3 = 5
print(f"The {k3}th largest element in {nums3} is: {kth_largest(nums3, k3)}")  # Output: 3
```

**Explanation:**

1. **`kth_largest(nums, k)` Function:**
   - Takes the list `nums` and the integer `k` as input.
   - Calculates `k_smallest_from_start` because `quickselect` is easier to implement when finding the *k*-th smallest element from the *beginning* of the array rather than the *k*-th largest element from the end.
   - Calls the `quickselect` helper function to recursively find the k-th smallest (or, equivalently, the (n-k+1)-th largest) element.

2. **`quickselect(l, r, k)` Function (Recursive):**
   - Base Case: If `l == r`, it means we've narrowed down the search to a single element, so we return it.
   - Calls `partition(l, r)` to partition the subarray `nums[l...r]` around a pivot.
   - Checks the position of the pivot after partitioning:
     - If `k` is the index of the pivot + 1 (because `k` is 1-indexed), then the pivot is the k-th smallest element, so we return it.
     - If `k` is less than the index of the pivot + 1, it means the k-th smallest element is in the left subarray, so we recursively call `quickselect` on the left subarray.
     - Otherwise, the k-th smallest element is in the right subarray, so we recursively call `quickselect` on the right subarray.

3. **`partition(l, r)` Function:**
   - Chooses the last element `nums[r]` as the pivot.  (You could choose a random pivot for better average-case performance, but this version is simpler.)
   - Iterates through the subarray from `l` to `r - 1`.
   - If an element `nums[j]` is less than or equal to the pivot, it's swapped to the left side of the subarray (before the `i` index).
   - Finally, the pivot is placed in its correct sorted position (between the elements less than it and the elements greater than it).
   - Returns the index of the pivot.

**Key Idea (QuickSelect):**

The QuickSelect algorithm is based on the same principle as QuickSort, but instead of recursively sorting both sides of the pivot, it only recurses into the side that contains the k-th smallest element.  This makes it more efficient because it avoids unnecessary sorting.  Its average time complexity is O(n), but its worst-case time complexity is O(n^2) if the pivot selection is consistently bad (e.g., always picking the smallest or largest element). Using a randomized pivot selection strategy improves the practical performance and makes the worst-case less likely.
**Time Complexity:**

*   **Average Case:** O(n) - Due to the QuickSelect algorithm.
*   **Worst Case:** O(n^2) -  If the pivot choice in the partitioning step is consistently bad (e.g., always the smallest or largest element).
*   **Space Complexity:** O(log n) - Average case for the recursion stack of quickselect. O(n) in the worst case.
This solution avoids built-in sorting functions and implements the QuickSelect algorithm, which is suitable for this type of problem.  It's an efficient and commonly used approach for finding the k-th largest (or smallest) element in an unsorted array.
