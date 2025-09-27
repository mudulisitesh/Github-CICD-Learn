Okay, here's a DSA problem and a Python solution:

**Problem:  First Missing Positive**

Given an unsorted integer array `nums`, find the smallest missing positive integer.  You must implement an algorithm that runs in `O(n)` time and uses constant extra space.

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

The problem requires us to find the smallest positive integer that's *not* present in the array.  A naive approach might involve sorting, but sorting is typically O(n log n).  We need an O(n) solution.  The key is to use the array itself as a hash table.

**Python Solution:**

```python
def first_missing_positive(nums):
    """
    Finds the smallest missing positive integer in an array.

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
    # After this conversion, `nums` will contain only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # 3. Use the index as a hash key and number sign as a presence detector.
    # For example, if nums[1] is negative, that means that the number `1`
    # is present in the array.
    # If nums[2] is positive, the number 2 is missing.
    for i in range(n):
        a = abs(nums[i])
        # If you meet number a in the array, change the sign of a-th element.
        # Be careful with duplicates: do it only once.
        if a == n:  # Edge case:  n itself
            nums[0] = - abs(nums[0]) #Use index 0 to mark n.
        else:
            nums[a] = - abs(nums[a])

    # 4. Now the index of the first positive number will be equal to
    # the first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0: #Check if n is missing.
        return n

    return n + 1  # If nums[0] is negative, then n+1 is missing.

# Example Usage:
nums1 = [1, 2, 0]
print(f"Input: {nums1}, Output: {first_missing_positive(nums1)}")  # Output: 3

nums2 = [3, 4, -1, 1]
print(f"Input: {nums2}, Output: {first_missing_positive(nums2)}")  # Output: 2

nums3 = [7, 8, 9, 11, 12]
print(f"Input: {nums3}, Output: {first_missing_positive(nums3)}")  # Output: 1

nums4 = [1]
print(f"Input: {nums4}, Output: {first_missing_positive(nums4)}") #Output: 2

nums5 = [2]
print(f"Input: {nums5}, Output: {first_missing_positive(nums5)}") #Output: 1

nums6 = [2,2]
print(f"Input: {nums6}, Output: {first_missing_positive(nums6)}") #Output: 1

nums7 = [1,1]
print(f"Input: {nums7}, Output: {first_missing_positive(nums7)}") #Output: 2
```

**Explanation of the Code:**

1. **Handle the Base Case (1):** The first thing we check is whether the number `1` is present in the array. If it's not, then `1` is the smallest missing positive, and we return it immediately.

2. **Clean Up the Array:** We iterate through the array and replace all negative numbers, zeros, and numbers greater than `n` (the array length) with `1`. This is crucial because we are going to use the array indices (1 to n) to represent the presence of numbers from 1 to n. Numbers outside this range are irrelevant.

3. **Using the Array as a Hash Table:** This is the core of the algorithm.  We iterate through the (modified) array.  For each number `a` in the array, we take its absolute value (`abs(nums[i])`).  We then treat `a` as an index into the array (`nums[a]`).  We change the sign of the element at that index to negative.  This "marks" the presence of the number `a` in the array.

   - **Important Note:** We're using the array *itself* to track which numbers (1 to n) are present.  A negative sign at `nums[i]` means the number `i` is present.
   - **Edge Case: n:** When `a` equals `n` (the length of the array), we have to use index 0 to mark the presence of n because index n doesn't exist. We use the sign of nums[0] for this.
   - **`abs()`:** We use `abs()` because the element at `nums[a]` might have already been changed to negative during a previous iteration.

4. **Finding the Missing Number:** After the previous step, the index of the first positive number in the array (starting from index 1) will be the smallest missing positive integer.  We iterate through the array (starting from index 1).  If we find a positive number `nums[i]`, it means that the number `i` is missing.

5. **Handle Edge Cases (n and n+1):**
   - If we make it through the loop from 1 to `n-1` and find no positive numbers, we check if `nums[0]` is positive. If it is, then `n` is missing.
   - If `nums[0]` is negative, it means that `n` is present. In this case, `n + 1` is the smallest missing positive.

**Time and Space Complexity:**

*   **Time Complexity:** O(n) - The algorithm iterates through the array a maximum of three times.
*   **Space Complexity:** O(1) - The algorithm uses constant extra space. We're modifying the array in-place.
