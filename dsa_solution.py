Okay, here's a DSA problem and a Python solution:

**Problem:**

**Rotate Array**

Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

**Constraints:**

*   `1 <= nums.length <= 10^5`
*   `-2^31 <= nums[i] <= 2^31 - 1`
*   `0 <= k <= 10^5`

**Python Solution:**

```python
def rotate_array(nums, k):
  """
  Rotates an array to the right by k steps.

  Args:
    nums: A list of integers.
    k: The number of steps to rotate the array to the right.

  Returns:
    None. Modifies the nums list in-place.
  """
  n = len(nums)
  k = k % n  # Handle cases where k > n

  nums[:] = nums[n-k:] + nums[:n-k] # In-place Rotation
  # can also use a helper function to reverse parts of array. see code below

#alternate solution using reverse method for in place rotation in O(n)
def rotate_array_reverse(nums, k):
    n = len(nums)
    k %= n

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


# Example usage:
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate_array(nums1, k1)
print(f"Rotated array (method 1): {nums1}")  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
k2 = 2
rotate_array_reverse(nums2, k2)
print(f"Rotated array (method 2): {nums2}")  # Output: [3, 99, -1, -100]

nums3 = [1,2,3]
k3 = 5
rotate_array_reverse(nums3, k3)
print(f"Rotated array (method 2): {nums3}") #Output: [2, 3, 1]
```

**Explanation:**

1.  **Modulo Operator:** `k = k % n` is crucial.  If `k` is larger than the array length `n`, we only need to rotate by the remainder after dividing `k` by `n`.  For example, rotating an array of length 7 by 10 steps is the same as rotating it by 3 steps.

2.  **In-Place Rotation (Slicing):**  `nums[:] = nums[n-k:] + nums[:n-k]` This creates a new array by concatenating two slices of the original array and assigns it back to the original array using slice assignment `[:]`. This modifies the original array in-place. We're taking the last `k` elements and putting them at the beginning.
    *   `nums[n-k:]`:  This slice gets the last `k` elements of the array.
    *   `nums[:n-k]`: This slice gets the first `n-k` elements of the array.
    *  The two parts are then concatenated in the correct order to get the rotated array.

3. **In-Place Rotation (Reversal):** The reverse method works by first reversing the entire array, then reversing the first k elements, and then reversing the remaining n-k elements.

**Time and Space Complexity:**

*   **Slicing Method:**
    *   Time Complexity: O(n) (due to creating slices and concatenating).
    *   Space Complexity: O(1) -  Though we create new lists, `nums[:] = ...` is done in-place by reassigning the values of the original `nums` list.  If we did `nums = nums[n-k:] + nums[:n-k]` the space complexity would be O(n).

*   **Reversal Method:**
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
This is because it modifies the array directly using reversals without creating extra copies of the array.

**Why this solution is good:**

*   **Clear and Readable:** The slicing-based solution is very concise and easy to understand. The reversal is also easy to read once you understand the logic behind it.
*   **In-Place:** Modifies the original array, which is often a requirement in interview settings.
*   **Handles edge cases:**  Correctly handles cases where `k` is larger than the array length.
