Okay, here's a DSA problem and its solution in Python:

**Problem:**

**Largest Subarray with Zero Sum**

Given an array of integers `nums`, find the length of the largest contiguous subarray that sums to zero.

**Example:**

```
Input: nums = [15, -2, 2, -8, 1, 7, 10, 23]
Output: 5
Explanation: The longest subarray with elements summing up to 0 is [-2, 2, -8, 1, 7] and has length 5.
```

**Solution in Python:**

```python
def max_len_subarray_zero_sum(nums):
    """
    Finds the length of the largest subarray with a zero sum.

    Args:
        nums: A list of integers.

    Returns:
        The length of the largest subarray with a zero sum.
    """

    max_length = 0
    sum_map = {0: -1}  # Store the first occurrence of each cumulative sum
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num

        if current_sum in sum_map:
            length = i - sum_map[current_sum]
            max_length = max(max_length, length)
        else:
            sum_map[current_sum] = i

    return max_length

# Example Usage
nums = [15, -2, 2, -8, 1, 7, 10, 23]
result = max_len_subarray_zero_sum(nums)
print(f"The length of the largest subarray with zero sum is: {result}")  # Output: 5

nums2 = [4, 2, -3, 1, 6]
result2 = max_len_subarray_zero_sum(nums2)
print(f"The length of the largest subarray with zero sum is: {result2}")  # Output: 0

nums3 = [0, 0, 0, 0]
result3 = max_len_subarray_zero_sum(nums3)
print(f"The length of the largest subarray with zero sum is: {result3}")  # Output: 4

nums4 = [ -1, 1, -1, 1]
result4 = max_len_subarray_zero_sum(nums4)
print(f"The length of the largest subarray with zero sum is: {result4}") #Output: 4

```

**Explanation:**

1. **`max_len_subarray_zero_sum(nums)` function:**
   - Takes a list of integers `nums` as input.
   - Initializes `max_length` to 0 (to store the maximum length found so far).
   - Initializes `sum_map` to `{0: -1}`. This dictionary will store the first occurrence of each cumulative sum encountered while iterating through the array.  The key is the cumulative sum, and the value is the index at which that sum was first encountered. The initial entry `0: -1` handles the case where a subarray starting from index 0 has a sum of 0.  This allows correctly calculating the length of that subarray.
   - Initializes `current_sum` to 0. This variable will keep track of the cumulative sum as we iterate.

2. **Iteration:**
   - The code iterates through the `nums` array using a `for` loop with `enumerate` to get both the index `i` and the value `num`.
   - `current_sum += num`: The cumulative sum is updated by adding the current element.

3. **Checking for Zero Sum Subarrays:**
   - `if current_sum in sum_map:`:  This is the core logic. If the `current_sum` is already present in the `sum_map`, it means that the subarray between the previous occurrence of this sum and the current index sums to zero.
     - `length = i - sum_map[current_sum]`: Calculate the length of this zero-sum subarray. The length is the difference between the current index `i` and the index of the previous occurrence of the `current_sum` (stored in `sum_map[current_sum]`).
     - `max_length = max(max_length, length)`: Update `max_length` if the current zero-sum subarray is longer than the previously found maximum length.

4. **Storing Cumulative Sums:**
   - `else:`: If the `current_sum` is *not* in the `sum_map`, it means we haven't seen this cumulative sum before.
     - `sum_map[current_sum] = i`: Store the `current_sum` and its corresponding index `i` in the `sum_map`.  This records the first time we encounter this sum.

5. **Return Value:**
   - After iterating through the entire array, the function returns the `max_length`, which represents the length of the largest contiguous subarray with a zero sum.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the array. The algorithm iterates through the array once.  The dictionary operations (`in` and assignment) take, on average, O(1) time.

- **Space Complexity:** O(n), where n is the length of the array.  In the worst case, `sum_map` might store all n cumulative sums if there are no repeating cumulative sums.  So, the space required by `sum_map` grows linearly with n.
