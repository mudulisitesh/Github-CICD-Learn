Okay, here's a randomly generated DSA problem and a Python solution:

**Problem:  "Longest Substring with At Most K Distinct Characters"**

**Description:**

Given a string `s` and an integer `k`, find the length of the longest substring of `s` that contains at most `k` distinct characters.

**Example:**

```
s = "eceba"
k = 2
```

The longest substring containing at most 2 distinct characters is "ece" with a length of 3.

**Constraints:**

*   `1 <= s.length <= 10^5`
*   `0 <= k <= 50`
*   `s` consists of lowercase English letters.

**Python Solution (Sliding Window Approach):**

```python
def longest_substring_with_k_distinct(s: str, k: int) -> int:
    """
    Finds the length of the longest substring of s with at most k distinct characters.

    Args:
        s: The input string.
        k: The maximum number of distinct characters allowed.

    Returns:
        The length of the longest substring.
    """

    if k == 0:
        return 0

    window_start = 0
    max_length = 0
    char_frequency = {}  # Store the frequency of characters in the current window

    for window_end in range(len(s)):
        right_char = s[window_end]
        char_frequency[right_char] = char_frequency.get(right_char, 0) + 1

        while len(char_frequency) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]  # Remove char if frequency is 0
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)  # Update max_length

    return max_length

# Example usage:
s = "eceba"
k = 2
result = longest_substring_with_k_distinct(s, k)
print(f"Longest substring with at most {k} distinct characters in '{s}': {result}") # Output: 3

s = "aaabbb"
k = 1
result = longest_substring_with_k_distinct(s,k)
print(f"Longest substring with at most {k} distinct characters in '{s}': {result}") # Output: 3

s = "abaccc"
k = 2
result = longest_substring_with_k_distinct(s,k)
print(f"Longest substring with at most {k} distinct characters in '{s}': {result}") # Output: 4

s = "a"
k = 0
result = longest_substring_with_k_distinct(s,k)
print(f"Longest substring with at most {k} distinct characters in '{s}': {result}") # Output: 0
```

**Explanation:**

1.  **Initialization:**
    *   `window_start`:  Index of the start of the sliding window (initially 0).
    *   `max_length`:  Length of the longest substring found so far (initially 0).
    *   `char_frequency`: A dictionary to store the frequency of each character in the current window.

2.  **Sliding Window:**
    *   The code iterates through the string using `window_end` as the index of the end of the sliding window.
    *   For each character at `window_end`, we update its frequency in the `char_frequency` dictionary.

3.  **Maintaining the Constraint:**
    *   The `while` loop ensures that the number of distinct characters in the `char_frequency` dictionary does not exceed `k`.
    *   If the number of distinct characters exceeds `k`, we shrink the window from the left (`window_start`).
    *   We decrement the frequency of the character at `window_start` in `char_frequency`. If the frequency becomes 0, we remove the character from the dictionary.
    *   We increment `window_start` to move the window's starting position.

4.  **Updating Maximum Length:**
    *   After each iteration (or when the number of distinct characters is within the limit), we update `max_length` with the maximum length of the current window ( `window_end - window_start + 1`).

5.  **Return Value:**
    *   Finally, the function returns the `max_length`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  In the worst case, each character in the string is visited twice (once by `window_end` and possibly once by `window_start`).
*   **Space Complexity:** O(k), where k is the maximum number of distinct characters allowed.  In the worst case, the `char_frequency` dictionary will store up to `k` distinct characters. In cases where k is similar or equal to the number of unique characters in `s`, the space complexity might be closer to O(number of unique characters). In practice, since k is capped at 50, the space complexity is considered effectively O(1).
