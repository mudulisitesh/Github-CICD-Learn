Okay, here's a randomly generated DSA problem and a Python solution:

**Problem:  First Missing Positive**

Given an unsorted integer array `nums`, find the smallest missing positive integer. You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

**Example 1:**

```
Input: nums = [1,2,0]
Output: 3
```

**Example 2:**

```
Input: nums = [3,4,-1,1]
Output: 2
```

**Example 3:**

```
Input: nums = [7,8,9,11,12]
Output: 1
```

**Explanation:**

The task is to efficiently find the smallest positive integer (greater than 0) that is missing from the given array. The constraints of O(n) time and O(1) space make it a bit tricky. We need to modify the array in-place to achieve this.
**Python Solution:**

```python
def firstMissingPositive(nums):
    """
    Finds the smallest missing positive integer in O(n) time and O(1) space.

    Args:
        nums: A list of integers.

    Returns:
        The smallest missing positive integer.
    """

    n = len(nums)

    # 1. Check if 1 is present. If not, you're done and 1 is the answer.
    if 1 not in nums:
        return 1

    # 2. Replace negative numbers, zeros, and numbers larger than n by 1.
    # After this conversion, nums will contain only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # 3. Use index as a hash key and number sign as a presence detector.
    # For example, if nums[1] is negative, that means that the number `1`
    # is present in the array.
    # If nums[2] is positive, the number 2 is missing.
    for i in range(n):
        a = abs(nums[i])
        # If you meet number a in the array, change the sign of the a-th element.
        # Be careful with duplicates: do it only once.
        if a == n:
            nums[0] = - abs(nums[0])  # Handle n at index 0
        else:
            nums[a] = - abs(nums[a])

    # 4. Now the index of the first positive number
    # will correspond to the first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1  # If nums[0] is negative, then n is missing

# Example Usage:
nums1 = [1, 2, 0]
print(f"Input: {nums1}, Output: {firstMissingPositive(nums1)}")  # Output: 3

nums2 = [3, 4, -1, 1]
print(f"Input: {nums2}, Output: {firstMissingPositive(nums2)}")  # Output: 2

nums3 = [7, 8, 9, 11, 12]
print(f"Input: {nums3}, Output: {firstMissingPositive(nums3)}")  # Output: 1

nums4 = [1]
print(f"Input: {nums4}, Output: {firstMissingPositive(nums4)}") #Output: 2

nums5 = [2]
print(f"Input: {nums5}, Output: {firstMissingPositive(nums5)}") #Output: 1
```

**Explanation of the Solution:**

1. **Check for 1:**  The algorithm first checks if `1` is present in the array. If it's not, then `1` is the missing positive.

2. **Data Cleaning:**  It replaces negative numbers, zeros, and numbers greater than `n` (the array's length) with `1`. This is crucial because we are going to use the array indices to mark the presence of numbers from 1 to `n`.

3. **Hashing with Sign:** This is the core idea.  We iterate through the array. For each number `a` (its absolute value), we change the sign of the element at index `a`.  Specifically:
   - If `a` is equal to `n`, we change the sign of `nums[0]` because we don't have an index `n`.
   - Otherwise, we change the sign of `nums[a]` (to mark the presence of `a`).

   The sign change acts as a marker to indicate that a particular number has been seen.  We use `abs()` to avoid changing the sign multiple times for duplicates.

4. **Finding the Missing Positive:** We iterate through the array again, starting from index 1. The first index `i` where `nums[i]` is positive means that the number `i` is missing.

5. **Edge Cases:**
   - If `nums[0]` is positive after the hashing, it means `n` is missing.
   - If all elements from index 1 to n-1 are negative, it means `n+1` is missing.

**Time and Space Complexity:**

*   **Time Complexity:** O(n) - The algorithm iterates through the array a constant number of times (3 times at most).
*   **Space Complexity:** O(1) - It modifies the array in-place and doesn't use any extra auxiliary space.
