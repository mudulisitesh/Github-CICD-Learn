Okay, here's a DSA problem involving array manipulation and a working Python solution:

**Problem:  Rotate Array**

Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example:**

*   `nums = [1,2,3,4,5,6,7], k = 3`
*   `Output: [5,6,7,1,2,3,4]`

**Explanation:**

Rotate 1 step to the right: `[7,1,2,3,4,5,6]`
Rotate 2 steps to the right: `[6,7,1,2,3,4,5]`
Rotate 3 steps to the right: `[5,6,7,1,2,3,4]`

**Constraints:**

*   `1 <= nums.length <= 10^5`
*   `-10^9 <= nums[i] <= 10^9`
*   `0 <= k <= 10^5`

**Python Code Solution:**

```python
def rotate_array(nums, k):
    """
    Rotates an array to the right by k steps.

    Args:
        nums: The array of integers to rotate.
        k: The number of steps to rotate the array.

    Returns:
        None.  Modifies the array in-place.
    """

    n = len(nums)
    k = k % n  # Effective rotation amount (handle cases where k > n)

    # Reverse the entire array
    nums[:] = nums[::-1]  # In-place reversal using slicing

    # Reverse the first k elements
    nums[:k] = nums[:k][::-1]

    # Reverse the remaining n-k elements
    nums[k:] = nums[k:][::-1]
```

**Explanation of the Code:**

1.  **Handle Large `k`:**
    *   `k = k % n` ensures that `k` is within the bounds of the array's length. If `k` is larger than the array length, we only need to rotate by the remainder. For example, rotating an array of length 7 by 9 positions is the same as rotating it by 2 positions.

2.  **Reverse the Entire Array:**
    *   `nums[:] = nums[::-1]` reverses the whole array in-place.  `[::-1]` creates a reversed copy of the array, and the `nums[:]` assignment replaces the original array's contents with the reversed copy.

3.  **Reverse the First `k` Elements:**
    *   `nums[:k] = nums[:k][::-1]` reverses the first `k` elements of the array.  This puts the elements that will be at the end of the rotated array into their correct positions.

4.  **Reverse the Remaining `n-k` Elements:**
    *   `nums[k:] = nums[k:][::-1]` reverses the remaining elements from index `k` to the end of the array. This puts the original beginning elements into their rotated positions.

**Why this approach works (Proof/Intuition):**

Let's say we have an array `[1, 2, 3, 4, 5]` and `k = 2`.

1.  **Reverse the entire array:** `[5, 4, 3, 2, 1]`
2.  **Reverse the first `k` elements (first 2):** `[4, 5, 3, 2, 1]`
3.  **Reverse the remaining elements:** `[4, 5, 1, 2, 3]`  This is the rotated array.

The idea is based on the observation that rotating an array can be achieved by strategically reversing parts of it.  Reversing the entire array, then reversing the first `k` elements, and then reversing the rest `(n-k)` of the array, effectively shifts the last `k` elements to the beginning and shifts the rest to the end.

**Example Usage:**

```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums = [-1,-100,3,99]
k = 2
rotate_array(nums,k)
print(nums) # Output: [3, 99, -1, -100]
```

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the array. Each reversal operation takes O(n) time, and we perform three reversals.
*   **Space Complexity:** O(1). The algorithm operates in-place, meaning it modifies the original array without using any significant extra space.  The reversal is done by swapping elements.
