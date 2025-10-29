Okay, here's a randomly generated DSA problem and a corresponding Python solution:

**Problem:**

**Longest Consecutive Sequence with Duplicates Allowed**

Given an unsorted list of integers, `nums`, find the length of the longest consecutive sequence of numbers that can be formed.  Numbers can appear multiple times within the list, and they contribute to the length. The consecutive sequence *must* include the given integers (i.e., no adding numbers).

**Example:**

```
nums = [100, 4, 200, 1, 3, 2, 1, 3, 5, 101, 102, 103, 102, 104]
```

The longest consecutive sequence is `[1, 2, 3, 4, 5]` which has a length of 5. Another consecutive sequence is `[100, 101, 102, 103, 104]` which also has a length of 5.

**Constraints:**

*   `0 <= nums.length <= 10^5`
*   `-10^9 <= nums[i] <= 10^9`

**Solution (Python):**

```python
def longest_consecutive_sequence(nums):
    """
    Finds the length of the longest consecutive sequence in a list of integers.

    Args:
      nums: A list of integers.

    Returns:
      The length of the longest consecutive sequence.
    """
    if not nums:
        return 0

    num_set = set(nums)  # Convert to set for O(1) lookup
    longest_streak = 0

    for num in nums:
        # Check if 'num' is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage:
nums = [100, 4, 200, 1, 3, 2, 1, 3, 5, 101, 102, 103, 102, 104]
result = longest_consecutive_sequence(nums)
print(f"Longest consecutive sequence length: {result}")  # Output: 5

nums2 = [0,3,7,2,5,8,4,6,0,1]
result2 = longest_consecutive_sequence(nums2)
print(f"Longest consecutive sequence length: {result2}")  # Output: 9

nums3 = [1,2,0,1]
result3 = longest_consecutive_sequence(nums3)
print(f"Longest consecutive sequence length: {result3}") # Output: 3
```

**Explanation:**

1.  **Convert to Set:**  We convert the input list `nums` into a set `num_set`.  This allows us to perform `O(1)` (constant time) lookups to check if a number exists in the input.

2.  **Iterate and Check for Start:**  We iterate through the original `nums` list. For each number `num`, we check if `num - 1` is *not* present in the `num_set`. This is crucial. If `num - 1` is *not* in the set, it means that `num` is potentially the *starting* point of a consecutive sequence. This prevents redundant checks and helps with optimization.

3.  **Extend the Sequence:** If `num` is a starting point, we initialize `current_num` to `num` and `current_streak` to 1.  We then enter a `while` loop that continues as long as `current_num + 1` is present in the `num_set`. Inside the loop, we increment `current_num` and `current_streak`. This effectively extends the consecutive sequence from the starting point.

4.  **Update Longest Streak:**  After the `while` loop completes (meaning the sequence has been fully extended), we update `longest_streak` by taking the maximum of the current `longest_streak` and the `current_streak`.

5.  **Return Result:** Finally, we return the `longest_streak`.

**Time Complexity:** O(n), where n is the length of the input list.  Although there is a nested `while` loop, each element is visited at most twice (once when it's iterated over in the main loop and at most once when it extends a sequence).

**Space Complexity:** O(n), because of the `num_set` which stores at most n elements.
