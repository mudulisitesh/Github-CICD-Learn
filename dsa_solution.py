Okay, here's a DSA problem with a Python solution:

**Problem:  Minimum Window Substring**

Given two strings `s` and `t`, find the minimum window substring in `s` which has all the characters of `t` in complexity O(n).

**Example:**

```
s = "ADOBECODEBANC"
t = "ABC"

Output: "BANC"
```

**Explanation:**

The minimum window substring "BANC" includes 'A', 'B', and 'C' from string `t`.

**Python Solution:**

```python
from collections import defaultdict

def min_window_substring(s, t):
    """
    Finds the minimum window substring in s containing all characters of t.

    Args:
        s: The string to search within.
        t: The string containing the characters to find.

    Returns:
        The minimum window substring, or an empty string if no such substring exists.
    """

    if not s or not t:
        return ""

    need = defaultdict(int)  # Characters we need to find and their counts
    for char in t:
        need[char] += 1

    window = defaultdict(int)  # Characters in the current window and their counts

    have = 0  # Number of required characters found in the window
    required = len(need)  # Number of distinct characters we need

    left = 0
    min_len = float('inf')
    start = 0  # Start index of the minimum window

    for right in range(len(s)):
        char = s[right]
        window[char] += 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == required:
            # Shrink the window from the left
            if (right - left + 1) < min_len:
                min_len = (right - left + 1)
                start = left

            left_char = s[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                have -= 1

            left += 1

    if min_len == float('inf'):
        return ""  # No valid window found
    else:
        return s[start : start + min_len]

# Example Usage:
s = "ADOBECODEBANC"
t = "ABC"
result = min_window_substring(s, t)
print(f"Minimum window substring: {result}") # Output: BANC

s = "a"
t = "aa"
result = min_window_substring(s, t)
print(f"Minimum window substring: {result}") # Output: ""

s = "a"
t = "a"
result = min_window_substring(s, t)
print(f"Minimum window substring: {result}") # Output: a

s = "ADOBECODEBANC"
t = "ABCC"  # Requires two Cs
result = min_window_substring(s, t)
print(f"Minimum window substring: {result}")  # Output: CODEBANC
```

**Explanation:**

1. **`need` Dictionary:** Stores the characters in `t` and their required counts.  For example, if `t = "ABCC"`, `need` will be `{'A': 1, 'B': 1, 'C': 2}`.

2. **`window` Dictionary:**  Keeps track of the characters in the current window (substring) and their counts.

3. **`have` and `required`:**
   - `have`: Counts how many of the *distinct* characters in `t` have met their required counts in the current window.
   - `required`: The number of *distinct* characters in `t`.

4. **Sliding Window:**
   - The `right` pointer expands the window.  For each character added to the window, its count is updated in the `window` dictionary.
   - If adding a character satisfies the required count for that character (`window[char] == need[char]`), we increment `have`.
   - The `while have == required` loop shrinks the window from the left (`left` pointer).  While all the required characters are in the window, we try to minimize the window size.  We update `min_len` and `start` if a smaller window is found.
   - Before moving `left`, we decrement the count of the character `s[left]` in the `window` dictionary.  If, after decrementing, the count of that character falls below its required count in `need`, we decrement `have`.

5. **Return Value:** If `min_len` remains `float('inf')`, it means no valid window was found, so we return an empty string. Otherwise, we return the substring `s[start : start + min_len]`.

**Time Complexity:** O(n), where n is the length of the string `s`.  Each pointer (`left` and `right`) moves through the string at most once.  The dictionary operations take O(1) on average.

**Space Complexity:** O(m), where m is the number of distinct characters in `t`. In the worst case (all characters in `t` are distinct), the space complexity can be O(1) since character sets are generally limited in size (e.g., ASCII).
