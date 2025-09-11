Okay, here's a random DSA problem and a Python solution:

**Problem:**

**Subarray with Given Sum**

Given an array of non-negative integers `arr` and a target sum `target`, find a contiguous subarray in `arr` whose elements sum up to `target`. If such a subarray exists, return the starting and ending indices (0-based) of the subarray. If no such subarray exists, return `[-1]`.

**Example:**

```
arr = [1, 4, 20, 3, 10, 5]
target = 33
Output: [2, 4]  (The subarray [20, 3, 10] sums up to 33)
```

**Python Solution:**

```python
def subarray_sum(arr, target):
    """
    Finds a contiguous subarray with the given sum.

    Args:
        arr: A list of non-negative integers.
        target: The target sum.

    Returns:
        A list containing the start and end indices of the subarray (0-based)
        or [-1] if no such subarray exists.
    """

    current_sum = 0
    start = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        while current_sum > target:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            return [start, i]

    return [-1]

# Example Usage:
arr = [1, 4, 20, 3, 10, 5]
target = 33
result = subarray_sum(arr, target)
print(result)  # Output: [2, 4]

arr = [1, 4, 0, 0, 3, 10, 5]
target = 7
result = subarray_sum(arr, target)
print(result) #output: [1, 4]

arr = [1, 4, 20, 3, 10, 5]
target = 3
result = subarray_sum(arr, target)
print(result) #Output: [3, 3]

arr = [1, 4, 20, 3, 10, 5]
target = 50
result = subarray_sum(arr, target)
print(result) #Output: [-1]
```

**Explanation:**

1. **`subarray_sum(arr, target)` function:**
   - `current_sum`:  Keeps track of the sum of the current subarray being considered.
   - `start`: Keeps track of the starting index of the current subarray.

2. **Sliding Window Approach:**
   - The outer `for` loop iterates through the array, expanding the window by including the current element `arr[i]` in the `current_sum`.
   - The `while` loop checks if `current_sum` exceeds the `target`. If it does, it shrinks the window from the left by removing elements (incrementing `start`) until `current_sum` is less than or equal to `target`.  This is the "sliding" part.
   - After adjusting the window, it checks if `current_sum` is equal to `target`. If it is, the function returns the `start` and `i` (end) indices of the subarray.

3. **No Subarray Found:**
   - If the loop completes without finding a subarray that sums to `target`, the function returns `[-1]`.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the array. The `for` loop iterates through the array once, and the `while` loop within the `for` loop processes each element at most once.
- **Space Complexity:** O(1).  The solution uses only a few extra variables (`current_sum`, `start`, `i`), so the space complexity is constant.

**Key Concepts Used:**

- **Sliding Window:**  This technique is effective for solving many array/string problems where you need to find a subarray or substring that satisfies a certain condition. The sliding window approach helps to avoid unnecessary recalculations by dynamically adjusting the window size.
- **Contiguous Subarray:** A subarray consisting of consecutive elements from the original array.
- **Non-negative Integers:**  The problem specifies that the input array contains non-negative integers.  This is important because it allows us to use the sliding window approach efficiently. If negative numbers were allowed, the sliding window technique would need to be modified to handle the possibility of `current_sum` decreasing when adding elements to the window, making the problem more complex (and potentially requiring a different approach like using a hash map to store prefix sums).
