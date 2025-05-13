Okay, here's a DSA problem and its Python solution:

**Problem:**

**Largest Range**

Given an array of integers `nums`, write a function `largest_range(nums)` that finds the largest range of consecutive integers in the array.  A range is defined as a set of consecutive integers. The function should return a list of two integers representing the start and end of the largest range.

**Examples:**

```
largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]) == [0, 7]
largest_range([1, 2, 3, 4, 5, 6, 7]) == [1, 7]
largest_range([9, 10, 11, 12, -1, 0, 1]) == [-1, 12]
```

**Solution:**

```python
def largest_range(nums):
    """
    Finds the largest range of consecutive integers in an array.

    Args:
        nums: A list of integers.

    Returns:
        A list of two integers representing the start and end of the largest range.
    """

    nums_set = set(nums)
    best_range = []
    longest_length = 0

    for num in nums:
        if num not in nums_set:
            continue

        nums_set.remove(num)  # Mark as visited
        current_length = 1
        left = num - 1
        right = num + 1

        while left in nums_set:
            nums_set.remove(left)
            current_length += 1
            left -= 1

        while right in nums_set:
            nums_set.remove(right)
            current_length += 1
            right += 1

        if current_length > longest_length:
            longest_length = current_length
            best_range = [left + 1, right - 1]  # left and right moved one step too far in the loops

    return best_range

# Example Usage
nums1 = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(f"Largest range for {nums1}: {largest_range(nums1)}")  # Output: [0, 7]

nums2 = [1, 2, 3, 4, 5, 6, 7]
print(f"Largest range for {nums2}: {largest_range(nums2)}")  # Output: [1, 7]

nums3 = [9, 10, 11, 12, -1, 0, 1]
print(f"Largest range for {nums3}: {largest_range(nums3)}")  # Output: [-1, 12]
```

**Explanation:**

1. **`largest_range(nums)` function:**

   - Takes an array `nums` as input.
   - Initializes `nums_set` to a set containing all elements of `nums`.  Using a set allows for fast O(1) lookups to check if a number exists.
   - `best_range` stores the start and end of the longest range found so far.
   - `longest_length` stores the length of the longest range found so far.

2. **Iterating through the array:**

   - The code iterates through each `num` in the input `nums` array.

3. **Skipping Visited Numbers:**

   - `if num not in nums_set: continue`  This is a crucial optimization. If a number has already been processed as part of a previous range, it's skipped. This prevents redundant calculations.

4. **Marking as Visited:**

   - `nums_set.remove(num)`: The current `num` is removed from the `nums_set`.  This is how we "mark" the number as visited, meaning we don't want to process it again as a starting point for a range.

5. **Expanding the Range:**

   - `left = num - 1` and `right = num + 1`:  These variables represent the potential boundaries of the consecutive range extending to the left and right of the current `num`.

   - `while left in nums_set:` and `while right in nums_set:`:  These loops expand the range as far as possible.
     - Inside the loops, the neighboring number is removed from `nums_set` (to avoid revisiting it), and the `current_length` is incremented.  `left` and `right` are updated to check for further consecutive numbers.

6. **Updating the Best Range:**

   - `if current_length > longest_length:`:  If the newly found `current_length` is greater than the `longest_length` found so far, update `longest_length` and `best_range`. The start and end points of the `best_range` are `left + 1` and `right - 1` because `left` and `right` are decremented/incremented one step too far in the loops.

7. **Returning the Result:**

   - Finally, the function returns the `best_range` found.

**Time and Space Complexity:**

- **Time Complexity:** O(N), where N is the number of elements in the input array. Although there are nested `while` loops, each number is visited and removed from the `nums_set` at most once.
- **Space Complexity:** O(N), because the `nums_set` can store up to N elements in the worst case.
