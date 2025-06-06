Okay, here's a DSA problem, along with a Python solution and explanation:

**Problem:**

**K-th Largest Element in an Array**

Given an unsorted array of integers `nums` and an integer `k`, find the *k*-th largest element in the array.

Note that it is the *k*-th largest element in the sorted order, not the *k*-th distinct element.

You must solve it in `O(n)` average time complexity.

**Example:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Python Solution (using Quickselect):**

```python
import random

def findKthLargest(nums, k):
    """
    Finds the k-th largest element in an array using the Quickselect algorithm.

    Args:
        nums: A list of integers.
        k: The index of the desired element (k-th largest).

    Returns:
        The k-th largest element in the array.
    """

    def quickselect(nums, left, right, k_smallest):
        """
        Recursive helper function for Quickselect.
        Finds the k_smallest-th smallest element within the subarray nums[left:right+1].
        """

        if left == right:
            return nums[left]

        # Choose a random pivot
        pivot_index = random.randint(left, right)
        pivot_index = partition(nums, left, right, pivot_index)  # Partition around the pivot

        if k_smallest == pivot_index:
            return nums[k_smallest]  # Found the element
        elif k_smallest < pivot_index:
            return quickselect(nums, left, pivot_index - 1, k_smallest)  # Search left subarray
        else:
            return quickselect(nums, pivot_index + 1, right, k_smallest)  # Search right subarray

    def partition(nums, left, right, pivot_index):
        """
        Partitions the subarray nums[left:right+1] around the pivot at pivot_index.
        Returns the new index of the pivot after partitioning.
        """

        pivot_value = nums[pivot_index]

        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        # Partition elements smaller than the pivot to the left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # Move pivot to its final sorted position
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    # Convert k-th largest to k-th smallest
    return quickselect(nums, 0, len(nums) - 1, len(nums) - k) #k_smallest = len(nums) - k


# Example usage:
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"The {k1}-th largest element in {nums1} is: {findKthLargest(nums1, k1)}")  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(f"The {k2}-th largest element in {nums2} is: {findKthLargest(nums2, k2)}")  # Output: 4

nums3 = [7,6,5,4,3,2,1]
k3 = 5
print(f"The {k3}-th largest element in {nums3} is: {findKthLargest(nums3,k3)}") #output : 3
```

**Explanation:**

1. **Quickselect Algorithm:**

   - Quickselect is a selection algorithm to find the *k*-th smallest element in an unordered list.  It is related to the Quicksort sorting algorithm but, instead of sorting the entire list, it only partitions the list around a pivot and then recursively searches in only one of the partitions.
   - The average time complexity is O(n) but the worst-case time complexity is O(n^2). To avoid the worst-case scenario, we use a randomized pivot.

2. **`findKthLargest(nums, k)` Function:**
   - It takes the input list `nums` and the integer `k` as parameters.
   - It calls the `quickselect()` helper function to do the actual work of finding the element.  Importantly, it transforms *k* (k-th largest) into the equivalent *k_smallest* value. If we want the k-th largest element, that's the same as finding the (n - k)-th smallest element, where n is the length of the array.

3. **`quickselect(nums, left, right, k_smallest)` Function (Recursive):**
   - `nums`: The list to search within.
   - `left`, `right`:  The boundaries of the subarray to search within (inclusive).
   - `k_smallest`: The index of the element we're looking for (k-th smallest).

   - **Base Case:** If `left == right`, it means the subarray has only one element, so we return that element.
   - **Pivot Selection:** A random element within the subarray is chosen as the pivot.  Using a random pivot helps to avoid worst-case performance (O(n^2)) when the input array is already sorted or nearly sorted.
   - **Partitioning:** The `partition()` function is called to rearrange the subarray around the pivot.  Elements smaller than the pivot are moved to the left of the pivot, and elements larger than the pivot are moved to the right.
   - **Recursive Calls:**
     - If `k_smallest` is equal to the pivot index, we've found the element we're looking for, so we return it.
     - If `k_smallest` is less than the pivot index, it means the k-th smallest element is in the left subarray, so we recursively call `quickselect()` on the left subarray.
     - If `k_smallest` is greater than the pivot index, it means the k-th smallest element is in the right subarray, so we recursively call `quickselect()` on the right subarray.

4. **`partition(nums, left, right, pivot_index)` Function:**
   - `nums`: The list to partition.
   - `left`, `right`:  The boundaries of the subarray to partition (inclusive).
   - `pivot_index`: The index of the pivot element.

   - **Pivot Placement:** It first moves the pivot element to the end of the subarray for convenience.
   - **Partitioning Loop:** It iterates through the subarray from `left` to `right - 1` (excluding the pivot at the end).  If an element is smaller than the pivot value, it swaps it with the element at `store_index`, effectively moving it to the left side of the subarray.
   - **Final Pivot Placement:** After the loop, it places the pivot element at its correct sorted position (at `store_index`).
   - **Return Value:** It returns the new index of the pivot element.

**Time and Space Complexity:**

*   **Time Complexity:**
    *   Average: O(n) - Quickselect on average partitions the array in half at each step.
    *   Worst: O(n^2) - Can occur if the pivot is consistently the smallest or largest element. Randomized pivot selection makes this very unlikely.
*   **Space Complexity:** O(1) - Quickselect is an in-place algorithm, meaning it uses a constant amount of extra space (excluding the input array).  The recursive calls use stack space, but the depth of the recursion is typically logarithmic (average case).
