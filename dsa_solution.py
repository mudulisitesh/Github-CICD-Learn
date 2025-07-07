Okay, here's a DSA problem and a Python solution:

**Problem:**

**Largest Range**

Given an array of integers, write a function that finds the largest range (inclusive) of integers contained in the array.  The range should be represented as a two-element array, `[first, last]`, where `first` is the first number in the range and `last` is the last number in the range.

A range `[a, b]` is considered larger than `[c, d]` if `(b - a) > (d - c)`.

You don't need to return the smallest such range if there are multiple ranges of the same size.

**Example:**

```
Input: array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Output: [0, 7]
```

**Explanation:**

The largest range of consecutive numbers in the input array is `[0, 1, 2, 3, 4, 5, 6, 7]`.
Therefore, the output is `[0, 7]`.

**Python Solution:**

```python
def largestRange(array):
    """
    Finds the largest range (inclusive) of integers contained in the array.

    Args:
        array: A list of integers.

    Returns:
        A list of two integers, representing the first and last number in the largest range.
    """

    nums = {}
    for num in array:
        nums[num] = True  # Mark each number as unvisited

    longest_range = [0, 0]
    max_length = 0

    for num in array:
        if not nums[num]:
            continue  # Skip already visited numbers

        nums[num] = False  # Mark as visited
        current_length = 1
        left = num - 1
        right = num + 1

        while left in nums:
            nums[left] = False
            current_length += 1
            left -= 1

        while right in nums:
            nums[right] = False
            current_length += 1
            right += 1

        if current_length > max_length:
            max_length = current_length
            longest_range = [left + 1, right - 1]

    return longest_range

# Example usage:
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
result = largestRange(array)
print(result)  # Output: [0, 7]

array2 = [4,2,1,3]
result2 = largestRange(array2)
print(result2) #Output: [1,4]
```

**Explanation of the Code:**

1. **`largestRange(array)` function:**
   - Takes the input array of integers.
   - Initializes a dictionary `nums` to store the presence of each number in the array.  Initially, all numbers are marked as `True` (unvisited).
   - Initializes `longest_range` to `[0, 0]` and `max_length` to 0. These will store the result and its length.

2. **Iteration:**
   - The code iterates through the input `array`.
   - **Check if Visited:** For each number `num` in the array, it checks if `nums[num]` is `False`.  If it's `False`, it means the number has already been visited as part of a previous range calculation, so it's skipped using `continue`.

3. **Mark as Visited and Expand Range:**
   - `nums[num] = False`: The current number `num` is marked as visited.
   - `current_length = 1`: The initial length of the range is set to 1 (just the current number itself).
   - `left = num - 1` and `right = num + 1`:  Pointers `left` and `right` are initialized to explore the numbers immediately to the left and right of `num`.

4. **Expand Left:**
   - `while left in nums:`:  This loop continues as long as numbers to the left of `num` exist in the `nums` dictionary (meaning they are present in the original array).
   - `nums[left] = False`: The number `left` is marked as visited.
   - `current_length += 1`: The length of the current range is incremented.
   - `left -= 1`: The `left` pointer moves further to the left.

5. **Expand Right:**
   - `while right in nums:`:  This loop does the same as the left loop, but expands the range to the right.

6. **Update Longest Range:**
   - `if current_length > max_length:`: If the `current_length` of the range found is greater than the `max_length` seen so far:
     - `max_length = current_length`: Update `max_length`.
     - `longest_range = [left + 1, right - 1]`: Update `longest_range` to the start and end of the new longest range.  We add 1 to `left` and subtract 1 from `right` because the `while` loops decrement `left` and increment `right` one too many times.

7. **Return:**
   - The function returns the `longest_range` found.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the input array. Although there are nested loops, each number in the array is visited and marked as visited only once.
- **Space Complexity:** O(n), where n is the length of the input array, due to the `nums` dictionary which stores all the numbers in the array.
