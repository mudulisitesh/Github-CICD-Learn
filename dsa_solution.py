Okay, here's a DSA problem, along with a Python solution.

**Problem:**

**Longest Substring Without Repeating Characters**

Given a string `s`, find the length of the longest substring without repeating characters.

**Example:**

*   **Input:** `s = "abcabcbb"`
*   **Output:** `3`
*   **Explanation:** The answer is "abc", with the length of 3.

*   **Input:** `s = "bbbbb"`
*   **Output:** `1`
*   **Explanation:** The answer is "b", with the length of 1.

*   **Input:** `s = "pwwkew"`
*   **Output:** `3`
*   **Explanation:** The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Solution (Python):**

```python
def length_of_longest_substring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """

    start = 0
    end = 0
    max_len = 0
    char_index_map = {}  # Stores the most recent index of each character

    while end < len(s):
        char = s[end]

        if char in char_index_map and char_index_map[char] >= start:
            # Repeating character found within the current window
            start = char_index_map[char] + 1  # Move start to after the previous occurrence
        else:
            # No repetition, so increment max_len if the current window is larger.
            max_len = max(max_len, end - start + 1)

        char_index_map[char] = end  # Update the index of the character
        end += 1

    return max_len


# Example Usage
string1 = "abcabcbb"
string2 = "bbbbb"
string3 = "pwwkew"

print(f"'{string1}': {length_of_longest_substring(string1)}")
print(f"'{string2}': {length_of_longest_substring(string2)}")
print(f"'{string3}': {length_of_longest_substring(string3)}")
```

**Explanation:**

1.  **`length_of_longest_substring(s)` function:**
    *   Initializes `start` and `end` pointers to 0.  These pointers define the sliding window.
    *   `max_len` keeps track of the maximum length found so far.
    *   `char_index_map` is a dictionary (hash map) to store the most recent index of each character encountered. This is crucial for efficiently checking for repeating characters within the current window.

2.  **`while end < len(s):` loop:**
    *   This loop iterates through the string using the `end` pointer.
    *   `char = s[end]` gets the character at the `end` position.
    *   **`if char in char_index_map and char_index_map[char] >= start:`:** This is the key part. It checks if the current character (`char`) is already in the `char_index_map` *and* if its last seen index (`char_index_map[char]`) is within the current window (`>= start`).
        *   If both conditions are true, it means we've encountered a repeating character within the current substring.
        *   We need to move the `start` pointer to `char_index_map[char] + 1`. This effectively shrinks the window to exclude the previous occurrence of the repeating character. The new window starts just after the previous occurrence.

    *   **`else:`:** If the character is not a repetition in the current window, it extends the window, so we update `max_len` to be the larger of the current `max_len` and the length of the current window (`end - start + 1`).

    *   `char_index_map[char] = end`:  Update the last seen index of the character in the `char_index_map`.  It doesn't matter if the character was already present or not; we always want to update to the *most recent* index.

    *   `end += 1`:  Move the `end` pointer to expand the window.

3.  **`return max_len`:** After iterating through the entire string, the function returns the maximum length of the substring without repeating characters.

**How it Works (Sliding Window):**

The algorithm uses a sliding window approach.  The `start` and `end` pointers define the window.  The `end` pointer always moves forward, expanding the window.  The `start` pointer only moves forward when a repeating character is found within the current window.  The `char_index_map` allows for efficient lookup of character indices, making the repetition check fast.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  Each character is visited at most twice (once by `end`, and possibly once when `start` is updated due to a repeated character).
*   **Space Complexity:** O(min(m, n)), where n is the length of the string `s`, and m is the size of the character set (e.g., 26 for lowercase English letters, 128 for ASCII, etc.). The `char_index_map` can store at most the number of distinct characters in the string.  In the worst case (all characters are distinct), the space complexity is O(n). However, if the character set is limited (e.g., only lowercase English letters), the space complexity is bounded by O(m), which would be a constant O(1) assuming m is fixed.  Since we consider the minimum, the complexity is O(min(m, n)).
