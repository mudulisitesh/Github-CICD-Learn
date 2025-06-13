Okay, here's a DSA problem that involves a combination of array manipulation and using a hash map (dictionary in Python) for efficient lookups.

**Problem: Find the Longest Subarray with Sum K**

**Description:**

Given an array of integers `nums` and an integer `k`, find the longest contiguous subarray whose sum equals `k`. Return the length of this subarray. If no such subarray exists, return 0.

**Example:**

```
nums = [1, -1, 5, -2, 3]
k = 3
Output: 4  (The subarray [1, -1, 5, -2] has sum 3 and length 4)

nums = [-2, -1, 2, 1]
k = 1
Output: 2 (The subarray [2,1] has sum 1 and length 2)
```

**Constraints:**

*   The length of the array can be up to 10<sup>5</sup>.
*   The array elements can be positive, negative, or zero.

**Python Code Solution:**

```python
def longest_subarray_with_sum_k(nums, k):
    """
    Finds the length of the longest contiguous subarray with sum k.

    Args:
        nums: A list of integers.
        k: The target sum.

    Returns:
        The length of the longest subarray with sum k, or 0 if no such subarray exists.
    """

    prefix_sum = 0
    max_len = 0
    prefix_sum_map = {0: -1}  # Key: prefix sum, Value: index where prefix sum occurs

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum - k in prefix_sum_map:
            max_len = max(max_len, i - prefix_sum_map[prefix_sum - k])

        if prefix_sum not in prefix_sum_map:  # Store only the *first* occurrence for longest length
            prefix_sum_map[prefix_sum] = i

    return max_len

# Example usage
nums1 = [1, -1, 5, -2, 3]
k1 = 3
print(f"Longest subarray length for nums = {nums1}, k = {k1}: {longest_subarray_with_sum_k(nums1, k1)}")  # Output: 4

nums2 = [-2, -1, 2, 1]
k2 = 1
print(f"Longest subarray length for nums = {nums2}, k = {k2}: {longest_subarray_with_sum_k(nums2, k2)}")  # Output: 2

nums3 = [5, 8, -4, -4, 9, -2, 2]
k3 = 0
print(f"Longest subarray length for nums = {nums3}, k = {k3}: {longest_subarray_with_sum_k(nums3, k3)}") # Output 3

nums4 = [0, 0, 0, 0, 0]
k4 = 0
print(f"Longest subarray length for nums = {nums4}, k = {k4}: {longest_subarray_with_sum_k(nums4, k4)}")  # Output: 5

nums5 = [2, 1, 0, 1, 3]
k5 = 0
print(f"Longest subarray length for nums = {nums5}, k = {k5}: {longest_subarray_with_sum_k(nums5, k5)}") # Output: 1
```

**Explanation:**

1.  **Prefix Sum:**  The core idea is to use prefix sums. `prefix_sum` at index `i` is the sum of elements from `nums[0]` to `nums[i]`.  If a subarray `nums[j+1...i]` has sum `k`, then `prefix_sum[i] - prefix_sum[j] = k`.  Therefore, `prefix_sum[j] = prefix_sum[i] - k`.

2.  **Hash Map (Dictionary):** We use a hash map `prefix_sum_map` to store prefix sums and their corresponding *first* indices. This allows us to quickly look up if a prefix sum `prefix_sum[i] - k` exists.

3.  **Algorithm:**
    *   Initialize `prefix_sum` to 0 and `max_len` to 0.  Create the `prefix_sum_map` and initialize it with `{0: -1}`.  The `0: -1` entry handles the case where the subarray starts from the beginning of the `nums` array.
    *   Iterate through the `nums` array.
    *   Update `prefix_sum`.
    *   Check if `prefix_sum - k` is in `prefix_sum_map`. If it is, it means there's a subarray ending at the current index `i` with a sum of `k`. Calculate the length of this subarray (`i - prefix_sum_map[prefix_sum - k]`) and update `max_len` if necessary.
    *   If the current `prefix_sum` is not in `prefix_sum_map`, add it with its index `i`. It's important to store only the *first* occurrence of each `prefix_sum` in the map.  This ensures that we find the *longest* subarray. If you store a later index, you would potentially be shortening the subarray unnecessarily.
    *   Return `max_len`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the `nums` array. We iterate through the array once.  Hash map lookups and insertions take O(1) on average.
*   **Space Complexity:** O(n) in the worst case.  The `prefix_sum_map` could potentially store all n prefix sums if they are all distinct.
