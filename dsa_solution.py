Okay, here's a randomly generated DSA problem and a Python solution.

**Problem:**

**Largest Contiguous Subarray Sum (Kadane's Algorithm)**

Given an array of integers (both positive and negative), find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Output: `6`
Explanation: `[4, -1, 2, 1]` has the largest sum = 6.

**Python Solution:**

```python
def max_subarray_sum(arr):
    """
    Finds the largest contiguous subarray sum using Kadane's Algorithm.

    Args:
        arr: A list of integers.

    Returns:
        The largest contiguous subarray sum.
    """

    max_so_far = float('-inf')  # Initialize to negative infinity
    current_max = 0

    for i in range(len(arr)):
        current_max += arr[i]

        if current_max > max_so_far:
            max_so_far = current_max

        if current_max < 0:
            current_max = 0

    return max_so_far

# Example Usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print(f"Largest contiguous subarray sum: {result}")  # Output: 6

arr2 = [-1, -2, -3, -4]
result2 = max_subarray_sum(arr2)
print(f"Largest contiguous subarray sum: {result2}")  # Output: -1
```

**Explanation:**

1. **Initialization:**
   - `max_so_far`:  Keeps track of the maximum sum found so far. It's initialized to negative infinity to handle cases where all elements are negative.
   - `current_max`:  Keeps track of the maximum sum ending at the current position.

2. **Iteration:**
   - The code iterates through the array.
   - `current_max += arr[i]`:  Adds the current element to the `current_max`.  We are extending the current subarray.
   - `if current_max > max_so_far:`: If the `current_max` is greater than the `max_so_far`, it means we've found a new maximum subarray sum.  So, we update `max_so_far`.
   - `if current_max < 0:`:  The crucial part of Kadane's Algorithm. If `current_max` becomes negative, it means including the current subarray (ending at the current position) will *decrease* the sum of any subsequent subarray.  Therefore, we reset `current_max` to 0, effectively starting a new subarray from the next element.

3. **Return:**
   - Finally, the function returns `max_so_far`, which holds the largest contiguous subarray sum found during the iteration.

**Why Kadane's Algorithm?**

Kadane's Algorithm is a dynamic programming approach that solves this problem in *O(n)* time complexity, which is the most efficient solution. It's based on the principle of finding optimal substructures. The optimal solution (largest sum) ending at each position depends on the optimal solution ending at the previous position.

**Edge Cases:**

*   **All Negative Numbers:** The algorithm correctly handles cases where all numbers in the array are negative.  In this scenario, it will return the largest (least negative) element in the array.  That is why we initialize `max_so_far` to negative infinity, otherwise the result could be zero.
