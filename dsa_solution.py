Okay, here's a DSA problem, along with a Python solution.

**Problem: Find the First Non-Repeating Character**

**Description:**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example 1:**

```
Input: s = "leetcode"
Output: 0
```

**Example 2:**

```
Input: s = "loveleetcode"
Output: 2
```

**Example 3:**

```
Input: s = "aabb"
Output: -1
```

**Python Solution:**

```python
def first_unique_char(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    char_counts = {}  # Dictionary to store character counts

    # Count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find the first character with a count of 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No non-repeating character found
# Test cases
print(first_unique_char("leetcode"))   # Output: 0
print(first_unique_char("loveleetcode")) # Output: 2
print(first_unique_char("aabb"))       # Output: -1
print(first_unique_char("dddccdbba")) #output: 8
```

**Explanation:**

1. **`first_unique_char(s)` function:**
   - Takes the input string `s` as an argument.
   - Initializes an empty dictionary `char_counts` to store the frequency of each character in the string.

2. **Character Counting:**
   - The first `for` loop iterates through the string `s`.
   - For each character `char`:
     - `char_counts.get(char, 0)` retrieves the current count of the character from the dictionary. If the character is not yet in the dictionary, it defaults to 0.
     - `+ 1` increments the count.
     - The updated count is stored back in the `char_counts` dictionary.

3. **Finding the First Unique Character:**
   - The second `for` loop iterates through the string `s` along with its index `i` using `enumerate()`.
   - For each character `char`:
     - `char_counts[char] == 1` checks if the count of the character in the dictionary is equal to 1.  If so, it means the character appears only once in the string.
     - If a unique character is found, its index `i` is returned immediately.

4. **No Unique Character:**
   - If the loop completes without finding a unique character (i.e., all characters appear more than once), the function returns -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(N), where N is the length of the string `s`.  We iterate through the string twice.
*   **Space Complexity:** O(K), where K is the number of distinct characters in the string `s`. In the worst case (where all characters are distinct), K = N. However, K can be at most the size of the character set (e.g., 26 for lowercase English letters).
This is a fairly common interview question and demonstrates a good use of dictionaries to efficiently track character frequencies.  It's also easy to understand and explain.
