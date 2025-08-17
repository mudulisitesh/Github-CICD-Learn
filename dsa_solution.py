Okay, here's a random DSA problem and a Python solution:

**Problem:**

**K-th Largest Element in an Array**

Given an unsorted array of integers `nums` and an integer `k`, find the k-th largest element in the array.  Note that it is the k-th largest element in sorted order, not the k-th distinct element.

For example:

*   `nums = [3, 2, 1, 5, 6, 4], k = 2`  Output: `5`
*   `nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4` Output: `4`

**Constraints:**

*   `1 <= k <= nums.length <= 10^5`
*   `-10^4 <= nums[i] <= 10^4`

**Python Solution (using Heap / Priority Queue):**

```python
import heapq

def find_kth_largest(nums, k):
    """
    Finds the k-th largest element in an array.

    Args:
        nums: A list of integers.
        k: An integer representing the k-th largest element to find.

    Returns:
        The k-th largest element in the array.
    """

    return heapq.nlargest(k, nums)[-1]

# Example Usage
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"The {k1}-th largest element in {nums1} is: {find_kth_largest(nums1, k1)}")  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(f"The {k2}-th largest element in {nums2} is: {find_kth_largest(nums2, k2)}")  # Output: 4

nums3 = [7,6,5,4,3,2,1]
k3 = 2
print(f"The {k3}-th largest element in {nums3} is: {find_kth_largest(nums3, k3)}")  #Output: 6
```

**Explanation:**

1.  **`heapq.nlargest(k, nums)`:**  The `heapq.nlargest()` function efficiently finds the `k` largest elements in the `nums` list.  It uses a heap data structure internally to achieve this. It constructs a min-heap of size `k` and keeps only the `k` largest elements seen so far in the array.  Elements smaller than the smallest element in the heap are ignored.

2.  **`[-1]`:** After obtaining the `k` largest elements (in descending order within that list), we access the last element (index -1) of the returned list from `heapq.nlargest(k, nums)`.  This last element is the k-th largest element in the original array.

**Time Complexity:** O(N log k), where N is the length of the `nums` array. This is because `heapq.nlargest` uses a heap of size `k`.

**Space Complexity:** O(k), as we're storing at most `k` elements in the heap.

**Alternative Solution (using Quickselect):**

While the heap-based solution is generally efficient, the quickselect algorithm (based on the partitioning step of quicksort) can potentially achieve O(N) average time complexity. Here's an implementation:

```python
import random

def quickselect(nums, k):
    """
    Finds the k-th largest element using the Quickselect algorithm.

    Args:
        nums: A list of integers.
        k: The k-th largest element to find.

    Returns:
        The k-th largest element in the array.
    """
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def select(left, right, k_smallest):
        """
        Performs recursive quickselect.

        Args:
            left: The left index of the subarray.
            right: The right index of the subarray.
            k_smallest: The index (starting from 0) of the k-th smallest element in the subarray.
        """
        if left == right:  # If the list contains only one element:
            return nums[left]

        # select a random pivot_index
        pivot_index = random.randint(left, right)

        # find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    n = len(nums)
    return select(0, n - 1, n - k)  # Find the (n-k)-th smallest element.  (n-k) indexes the k-th largest.


# Example usage:
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"The {k1}-th largest element (Quickselect) in {nums1} is: {quickselect(nums1, k1)}")  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(f"The {k2}-th largest element (Quickselect) in {nums2} is: {quickselect(nums2, k2)}")  # Output: 4

nums3 = [7,6,5,4,3,2,1]
k3 = 2
print(f"The {k3}-th largest element (Quickselect) in {nums3} is: {quickselect(nums3, k3)}")  #Output: 6
```

**Explanation of Quickselect:**

1.  **`partition(left, right, pivot_index)`:** This function is similar to the partition step in quicksort.  It chooses a pivot element, moves it to its correct sorted position in the subarray `nums[left:right+1]`, and returns the index of the pivot.

2.  **`select(left, right, k_smallest)`:** This is a recursive function.
    *   It picks a random pivot.  Randomization helps to avoid worst-case scenarios (O(N^2) time complexity).
    *   It partitions the array around the pivot.
    *   It checks if the pivot's index is equal to the desired `k_smallest` index.  If so, the pivot is the k-th smallest element (and therefore the (n-k)-th largest).
    *   If `k_smallest` is less than the pivot's index, it recursively calls `select` on the left subarray.
    *   If `k_smallest` is greater than the pivot's index, it recursively calls `select` on the right subarray.

3.  In the main `quickselect` function, we call `select` with `k_smallest = n - k` because finding the k-th *largest* element is equivalent to finding the (n-k)-th *smallest* element in a 0-indexed array.

**Time Complexity (Quickselect):**

*   **Average case:** O(N)
*   **Worst case:** O(N^2)  (Can occur if the pivot is consistently a bad choice, like always the smallest or largest element). Randomization mitigates this risk.

**Space Complexity (Quickselect):**

*   O(1) in-place (excluding the recursion stack, which can be O(log N) on average or O(N) in the worst case).
