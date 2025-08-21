Okay, here's a DSA problem along with a Python solution:

**Problem:**

**Maximum Subarray Sum with at Most K Elements**

Given an array of integers `nums` and an integer `k`, find the maximum sum of a contiguous subarray of `nums` that has at most `k` elements.

**Example:**

```
nums = [1, 3, -2, 5, -4, 2]
k = 3
```

The maximum subarray sum with at most 3 elements would be `1 + 3 + (-2) + 5 = 7` (Subarray: `[1, 3, -2, 5]` is incorrect because the problem specifies at MOST k elements).  `3 + (-2) + 5 = 6` is valid and is also not the maximum (or 1 + 3 = 4, 5 + (-4) + 2 = 3, etc). `[3, -2, 5]` sums to 6. The subarray `[5, -4, 2]` sums to 3.  `[1, 3]` sums to 4. `[3, -2]` sums to 1. `[1]` sums to 1. `[3]` sums to 3. `[-2]` sums to -2. `[5]` sums to 5. `[-4]` sums to -4. `[2]` sums to 2.  `[1, 3, -2]` sums to 2. The maximum sum is 6.

```
nums = [-1, -2, -3]
k = 2
```

The maximum subarray sum with at most 2 elements is -1.

**Constraints:**

*   `1 <= len(nums) <= 10^5`
*   `-10^4 <= nums[i] <= 10^4`
*   `1 <= k <= len(nums)`

**Python Solution:**

```python
def max_subarray_sum_k(nums, k):
    """
    Finds the maximum sum of a contiguous subarray of nums with at most k elements.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum number of elements allowed in the subarray.

    Returns:
        The maximum subarray sum.
    """

    max_sum = float('-inf')  # Initialize max_sum to negative infinity

    for i in range(len(nums)):  # Start index of the subarray
        current_sum = 0
        for j in range(i, min(i + k, len(nums))):  # End index of the subarray, ensuring it's at most k elements long
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum) # Update max_sum if current_sum is larger

    return max_sum


# Example usage:
nums1 = [1, 3, -2, 5, -4, 2]
k1 = 3
print(f"Max subarray sum for nums = {nums1}, k = {k1}: {max_subarray_sum_k(nums1, k1)}")  # Output: 6

nums2 = [-1, -2, -3]
k2 = 2
print(f"Max subarray sum for nums = {nums2}, k = {k2}: {max_subarray_sum_k(nums2, k2)}")  # Output: -1

nums3 = [5, -4, 2]
k3 = 2
print(f"Max subarray sum for nums = {nums3}, k = {k3}: {max_subarray_sum_k(nums3, k3)}") # Output 5

nums4 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
k4 = 3
print(f"Max subarray sum for nums = {nums4}, k = {k4}: {max_subarray_sum_k(nums4, k4)}") # Output: 6
```

**Explanation:**

1.  **Initialization:**
    *   `max_sum = float('-inf')`: We initialize `max_sum` to negative infinity to ensure that any valid subarray sum will be greater than the initial value.

2.  **Outer Loop (Start Index):**
    *   `for i in range(len(nums))`: This loop iterates through each element of the `nums` array, considering each element as a potential starting point for a subarray.

3.  **Inner Loop (End Index):**
    *   `for j in range(i, min(i + k, len(nums)))`: This loop iterates from the starting index `i` up to `i + k - 1` (inclusive), but it stops at `len(nums) - 1` if `i + k` exceeds the bounds of the array. This ensures that the subarray has at most `k` elements.  `min(i+k, len(nums))` makes sure we don't go out of bounds.  For instance, if `i` is `len(nums) - 1`, the inner loop will only execute once (j == i), giving us a subarray of length 1 (the last element of the array).

4.  **Calculating and Updating Sum:**
    *   `current_sum += nums[j]`: In each iteration of the inner loop, we add the current element `nums[j]` to the `current_sum`.
    *   `max_sum = max(max_sum, current_sum)`: We update `max_sum` to be the maximum between the current `max_sum` and the `current_sum`.  This ensures that `max_sum` always holds the largest subarray sum encountered so far.

5.  **Return Value:**
    *   `return max_sum`: Finally, we return the `max_sum`, which represents the maximum sum of any contiguous subarray with at most `k` elements.

**Time Complexity:** O(n\*k), where n is the length of `nums`.  In the worst case, the inner loop iterates up to `k` times for each element in the outer loop.

**Space Complexity:** O(1), because we are using only a constant amount of extra space.
