Okay, here's a random DSA problem and a Python solution:

**Problem:  First Missing Positive Integer**

Given an unsorted integer array `nums`, find the smallest missing positive integer.  The algorithm should run in O(n) time and use constant extra space.

**Example:**

```
Input: nums = [1,2,0]
Output: 3

Input: nums = [3,4,-1,1]
Output: 2

Input: nums = [7,8,9,11,12]
Output: 1
```

**Python Solution:**

```python
def firstMissingPositive(nums):
    """
    Finds the smallest missing positive integer in an array.

    Args:
        nums: A list of integers.

    Returns:
        The smallest missing positive integer.
    """

    n = len(nums)

    # 1. Basic checks and pre-processing:
    #  - If 1 is not present, 1 is the answer.
    if 1 not in nums:
        return 1

    #  - Replace negative numbers, zeros,
    #    and numbers larger than n by 1.
    #    After this conversion, nums will contain
    #    only positive numbers.  This is important for the index trick below.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # 2. Index as a hash key trick:
    #  - Iterate over the array.
    #  - Change the sign of the a-th element if you meet number a.
    #    Be careful with duplicates: do it only once.
    #  - Use index 0 to save information about the presence of number n
    #    since index n is not available.
    for i in range(n):
        a = abs(nums[i])
        if a == n:  # Special case to mark the presence of n
            nums[0] = - abs(nums[0])
        else:
            nums[a] = - abs(nums[a])  # Mark the presence of a.

    # 3. Find the index
    # - Now the index of the first positive number
    #   is equal to first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1 # All 1...n are present, then return n+1

# Example usage:
print(firstMissingPositive([1,2,0]))    # Output: 3
print(firstMissingPositive([3,4,-1,1]))   # Output: 2
print(firstMissingPositive([7,8,9,11,12]))  # Output: 1
print(firstMissingPositive([1,2,3]))      # Output: 4
print(firstMissingPositive([1]))        # Output: 2
print(firstMissingPositive([2]))        # Output: 1
print(firstMissingPositive([2, 1]))    # Output: 3
print(firstMissingPositive([1,1]))     # Output: 2
print(firstMissingPositive([1, 2, 2, 3, 3, 3]))  #Output: 4
```

**Explanation:**

1. **Handle Edge Cases and Preprocessing:**

   - First, we check if `1` is present in the array. If not, the smallest missing positive integer is `1`.
   - Then, we iterate through the array and replace any negative numbers, zeros, or numbers greater than `n` (the length of the array) with `1`. This ensures that we're dealing with positive integers in the range `[1, n]` for the next step.  This replacement is crucial for making the index-as-hash-key trick work.

2. **Index as Hash Key Trick:**

   - The core idea is to use the array indices as a hash table.  If we encounter a number `a` in the array (where `1 <= a <= n`), we change the sign of the element at index `a`.
   - We iterate through the array:
     - If the number is `n`, we negate `nums[0]` to indicate the presence of `n`. We use index `0` because index `n` is outside the bounds of the array.
     - Otherwise, we negate `nums[abs(nums[i])]`. `abs(nums[i])` is used in case we have already negated this index.

3. **Find the First Positive Index:**

   - After the above step, we iterate through the array again (starting from index `1`).
   - The first index `i` where `nums[i]` is positive indicates that the number `i` is missing.
   - If we reach the end of the loop without finding a positive number, it means all numbers from `1` to `n-1` are present.  We check if `nums[0]` is positive, if it is, `n` is missing.  If nums[0] is negative, n is present and the answer is `n+1`.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the input array.  We iterate through the array at most three times.
- **Space Complexity:** O(1), constant extra space. We modify the array in-place.

**Why this solution is clever:**

The ingenuity lies in using the array itself as a hash table to track the presence or absence of numbers in the range `[1, n]`.  By changing the sign of elements, we can mark the presence of a number without using any extra space.
