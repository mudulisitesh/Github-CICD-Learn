Okay, here's a DSA problem and a Python solution:

**Problem:  Maximum Sum Subarray (Kadane's Algorithm)**

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

*   **Input:** `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
*   **Output:** `6`
*   **Explanation:** `[4, -1, 2, 1]` has the largest sum = `6`.

**Python Solution (Kadane's Algorithm):**

```python
def max_subarray_sum(nums):
  """
  Finds the maximum sum of a contiguous subarray using Kadane's algorithm.

  Args:
      nums: A list of integers.

  Returns:
      The maximum sum of a contiguous subarray.
  """

  max_so_far = float('-inf')  # Initialize with negative infinity
  current_max = 0

  for num in nums:
    current_max = max(num, current_max + num) # either current element or current_max + current element is greater.
    max_so_far = max(max_so_far, current_max)

  return max_so_far

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print(f"Maximum subarray sum: {result}") # Output: Maximum subarray sum: 6

nums2 = [1]
result2 = max_subarray_sum(nums2)
print(f"Maximum subarray sum: {result2}") # Output: Maximum subarray sum: 1

nums3 = [-1]
result3 = max_subarray_sum(nums3)
print(f"Maximum subarray sum: {result3}") # Output: Maximum subarray sum: -1

nums4 = [-1, -2, -3]
result4 = max_subarray_sum(nums4)
print(f"Maximum subarray sum: {result4}") # Output: Maximum subarray sum: -1
```

**Explanation:**

1.  **Initialization:**
    *   `max_so_far`: This variable stores the maximum sum found so far. It's initialized to negative infinity because we want to ensure that even if all numbers in the array are negative, we find the least negative number's sum (which would be the maximum).
    *   `current_max`: This variable keeps track of the maximum sum ending at the current position in the array.  It's initialized to 0.

2.  **Iteration:**
    *   The code iterates through the `nums` array.
    *   `current_max = max(num, current_max + num)`: This is the core of Kadane's algorithm.  For each element `num`, we decide whether to:
        *   Start a new subarray from the current element (`num`). This is chosen if adding the current element to the existing `current_max` would make it smaller than the current element itself.
        *   Extend the previous subarray by adding the current element (`current_max + num`).
    *   `max_so_far = max(max_so_far, current_max)`: We update `max_so_far` with the maximum between the `max_so_far` we had so far and the new `current_max`.

3.  **Return:**
    *   Finally, the function returns `max_so_far`, which holds the maximum sum of any contiguous subarray found.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the input array, because we iterate through the array only once.
*   **Space Complexity:** O(1), because we use only a constant amount of extra space (for the `max_so_far` and `current_max` variables), regardless of the size of the input array.  This makes it a very efficient algorithm for this problem.
