Okay, here's a problem and a corresponding Python solution:

**Problem: First Missing Positive**

Given an unsorted integer array `nums`, find the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses constant extra space.

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

**Constraints:**

*   `1 <= nums.length <= 5 * 105`
*   `-231 <= nums[i] <= 231 - 1`
**Python Solution:**

```python
def firstMissingPositive(nums):
    """
    Finds the smallest missing positive integer in O(n) time and constant extra space.

    Args:
        nums: A list of integers.

    Returns:
        The smallest missing positive integer.
    """
    n = len(nums)

    # Check if 1 is present. If not, you're done and 1 is the answer.
    if 1 not in nums:
        return 1

    # Replace negative numbers, zeros,
    # and numbers larger than n by 1s.
    # After this conversion, nums will contain
    # only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # Use index as a hash key and number sign as a presence detector.
    # For example, if nums[1] is negative, that means that the number `1`
    # is present in the array.
    # If nums[2] is positive, the number 2 is missing.
    for i in range(n):
        a = abs(nums[i])
        # If you meet number a in the array, change the sign of the a-th element.
        # Be careful with duplicates: do it only once.
        if a == n:
            nums[0] = - abs(nums[0])  # Mark that `n` is present by flipping the sign of nums[0].
        else:
            nums[a] = - abs(nums[a])


    # Now the index of the first positive number
    # is equal to the first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1  # If nums[0] is negative, it means `n` is present.
```

**Explanation:**

1. **Check for 1:** If `1` is not in the array, we immediately return `1` because that's the smallest missing positive.

2. **Handle Invalid Numbers:** We replace all negative numbers, zeros, and numbers greater than `n` with `1`. This is because we're only interested in positive integers within the range `[1, n]`.  Numbers outside this range are irrelevant to the solution.

3. **Use Index as a Hash:** The core idea is to use the indices of the array to keep track of which numbers are present.
   - Iterate through the array. For each number `a = abs(nums[i])`, we treat `a` as an index.
   - If `a` is `n` (equal to the length of the array), we use `nums[0]` to store the information, because there is no index `n` in the `nums` array
   - Negate the element at index `a` (i.e., `nums[a]`). This indicates that the number `a` is present in the array.
   - We take the absolute value `abs()` of `nums[i]` to handle duplicate values and ensure we're always using a valid index.

4. **Find the First Positive Index:** After marking the presence of numbers, iterate through the array again, starting from index 1. The first positive element's index represents the smallest missing positive number.

5. **Handle n Case:** If all elements from `nums[1]` to `nums[n-1]` are negative, then the smallest missing positive is `n` if `nums[0]` is positive.  If `nums[0]` is negative, it means that `n` is present. Therefore, the smallest missing positive is `n + 1`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n) - The algorithm iterates through the array a few times.
*   **Space Complexity:** O(1) - It uses constant extra space. The modifications are done in-place.
**Example Usage:**

```python
nums1 = [1, 2, 0]
print(firstMissingPositive(nums1))  # Output: 3

nums2 = [3, 4, -1, 1]
print(firstMissingPositive(nums2))  # Output: 2

nums3 = [7, 8, 9, 11, 12]
print(firstMissingPositive(nums3))  # Output: 1

nums4 = [1]
print(firstMissingPositive(nums4)) # Output 2

nums5 = [1,2,3]
print(firstMissingPositive(nums5)) # Output 4
```
