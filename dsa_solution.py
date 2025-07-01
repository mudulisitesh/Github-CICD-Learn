Okay, here's a DSA problem focusing on array manipulation and a working Python solution.

**Problem:  Find the Missing Positive Integer**

Given an unsorted integer array `nums`, find the smallest missing positive integer. You must implement an algorithm that runs in `O(n)` time and uses constant extra space.

**Example:**

```
Input: nums = [1,2,0]
Output: 3

Input: nums = [3,4,-1,1]
Output: 2

Input: nums = [7,8,9,11,12]
Output: 1
```

**Explanation:**

The problem asks for the *smallest* positive integer that's *missing* from the given array. For instance, in `[1, 2, 0]`, 1 and 2 are present, so the smallest missing positive is 3. Constant extra space means we cannot use additional data structures that grow proportionally to the input size (e.g., no extra arrays, hash maps of size 'n', etc.).

**Python Solution:**

```python
def firstMissingPositive(nums):
    """
    Finds the smallest missing positive integer in an unsorted array.

    Args:
        nums: A list of integers.

    Returns:
        The smallest missing positive integer.
    """

    n = len(nums)

    # 1. Check if 1 is present. If not, you're done and 1 is the answer.
    if 1 not in nums:
        return 1

    # 2. Replace negative numbers, zeros,
    # and numbers larger than n by 1s.
    # After this conversion, nums will contain
    # only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # 3. Use the index as a hash key and the sign of the number as a presence detector.
    # For example, if nums[1] is negative, that means that the number `1`
    # is present in the array.
    # If nums[2] is positive, the number 2 is missing.
    for i in range(n):
        a = abs(nums[i])
        # If you meet the number a in the array, change the sign of the a-th element.
        # Be careful with duplicates: do it only once.
        if a == n:
            nums[0] = - abs(nums[0])  #Special Case for handling number 'n', we store the sign at index 0
        else:
            nums[a] = - abs(nums[a])

    # 4. Now the index of the first positive number
    # is equal to the first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1
# Example Usage:
nums1 = [1, 2, 0]
print(f"Input: {nums1}, Output: {firstMissingPositive(nums1)}") # Output: 3

nums2 = [3, 4, -1, 1]
print(f"Input: {nums2}, Output: {firstMissingPositive(nums2)}") # Output: 2

nums3 = [7, 8, 9, 11, 12]
print(f"Input: {nums3}, Output: {firstMissingPositive(nums3)}") # Output: 1

nums4 = [1]
print(f"Input: {nums4}, Output: {firstMissingPositive(nums4)}") # Output: 2

nums5 = [2]
print(f"Input: {nums5}, Output: {firstMissingPositive(nums5)}") # Output: 1

nums6 = [2,2]
print(f"Input: {nums6}, Output: {firstMissingPositive(nums6)}")
```

**Explanation of the Code:**

1. **Check for '1':**  The function first checks if `1` is present in the array. If not, `1` is the smallest missing positive, and we return immediately.

2. **Normalize the array:** Any numbers that are negative, zero, or greater than `n` (the array length) are replaced with `1`. The reason is that the smallest missing positive integer can only be between 1 and `n+1`. Numbers outside this range are irrelevant.

3. **Use Indexing as a Hash:** The core idea is to use the array indices as a kind of "hash table" to mark the presence of numbers. We iterate through the array. For each number `a` (the absolute value), we negate the element at index `a` (if `a` is within the bounds of the array). If `nums[a]` becomes negative, it means we've seen the number `a` in the array. If `a` equals the array length `n`, we negate `nums[0]` because we can't use index `n` (the array has indices from `0` to `n-1`).  Duplicates are handled because we only negate once.

4. **Find the First Positive Index:** After the previous step, the first index `i` (starting from `1`) where `nums[i]` is positive indicates that the number `i` is missing.  If `nums[0]` is positive, it means 'n' is missing.

5. **Handle Edge Cases:** If all elements from `nums[1]` to `nums[n-1]` are negative, it means the missing positive is `n + 1`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n) - The algorithm iterates through the array a few times.
*   **Space Complexity:** O(1) - The algorithm uses constant extra space. It modifies the input array in place.

**Key Ideas Used:**

*   **Hashing with Indexing:** Cleverly using array indices as a way to track the presence of numbers.
*   **In-Place Modification:** Modifying the input array directly to avoid extra memory usage.
*   **Handling Edge Cases:** Addressing scenarios where the missing number is 1 or greater than `n`.
