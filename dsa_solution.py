Okay, here's a DSA problem and a Python solution:

**Problem:**

**Find the Maximum Subarray Sum (Kadane's Algorithm)**

Given an array of integers, `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Python Solution (Kadane's Algorithm):**

```python
def max_subarray_sum(nums):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Args:
        nums: A list of integers.

    Returns:
        The maximum subarray sum.
    """

    max_so_far = float('-inf')  # Initialize to negative infinity to handle all negative arrays
    current_max = 0

    for num in nums:
        current_max = max(num, current_max + num)  # Either start a new subarray from current num or extend the previous one
        max_so_far = max(max_so_far, current_max)

    return max_so_far

# Example Usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print(f"Maximum subarray sum: {result}")  # Output: Maximum subarray sum: 6

nums2 = [-1, -2, -3]
result2 = max_subarray_sum(nums2)
print(f"Maximum subarray sum: {result2}") # Output: Maximum subarray sum: -1

nums3 = [5]
result3 = max_subarray_sum(nums3)
print(f"Maximum subarray sum: {result3}") # Output: Maximum subarray sum: 5
```

**Explanation:**

1.  **Initialization:**

    *   `max_so_far`:  This variable keeps track of the maximum subarray sum found so far.  It's initialized to negative infinity to correctly handle cases where all numbers in the array are negative (in which case the largest sum would be the least negative number).
    *   `current_max`: This variable keeps track of the maximum subarray sum ending at the current position. It's initialized to 0.

2.  **Iteration:**

    *   The code iterates through the `nums` array.
    *   `current_max = max(num, current_max + num)`:  This is the core of Kadane's Algorithm. For each number, we decide whether to:
        *   **Start a new subarray** from the current number (`num`). This happens if `num` is greater than the current running sum (`current_max + num`).  This means the previous subarray sum was dragging the total sum down, so we're better off starting fresh.
        *   **Extend the existing subarray** by adding the current number (`current_max + num`). This happens if adding the current number to the existing sum increases the overall sum.

    *   `max_so_far = max(max_so_far, current_max)`: We update `max_so_far` to be the larger of the current maximum sum found so far and the maximum sum ending at the current position.

3.  **Return Value:**

    *   The function returns `max_so_far`, which is the maximum sum of any contiguous subarray in the input array.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the array (because we iterate through the array once).
*   **Space Complexity:** O(1) (constant), because we only use a few extra variables (`max_so_far`, `current_max`) that do not depend on the size of the input array.

**Why Kadane's Algorithm is Efficient:**

Kadane's Algorithm provides an optimal O(n) solution to this problem. A naive approach of checking all possible subarrays would take O(n^2) or even O(n^3) time.  Kadane's Algorithm smartly avoids recomputing sums by keeping track of the `current_max` and efficiently updating `max_so_far`.
