Okay, here's a DSA problem and a Python solution:

**Problem:  First Unique Character in a String**

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
def first_unique_char(s: str) -> int:
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    char_counts = {}  # Dictionary to store character counts

    # Count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string again and check for the first unique character
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No unique character found


# Example usage
print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))

```

**Explanation:**

1. **`char_counts = {}`**:  A dictionary `char_counts` is initialized to store the frequency of each character in the string.

2. **Counting Character Frequencies:** The first `for` loop iterates through the input string `s`.  For each character `char`:
   - `char_counts.get(char, 0)`:  This attempts to retrieve the current count for the character `char` from the `char_counts` dictionary. If the character is not already a key in the dictionary, `get()` returns the default value of 0.
   - `+ 1`: The count is incremented by 1.
   - `char_counts[char] = ...`: The updated count is stored back into the `char_counts` dictionary with the character as the key.

3. **Finding the First Unique Character:** The second `for` loop iterates through the string `s` along with its indices using `enumerate(s)`.
   - `if char_counts[char] == 1:`:  For each character, it checks if its count in the `char_counts` dictionary is equal to 1.  If it is, this means the character appears only once in the string.
   - `return i`: If a unique character is found, its index `i` is immediately returned.

4. **No Unique Character Found:** If the loop completes without finding any character with a count of 1, the function returns -1.

**Time and Space Complexity:**

* **Time Complexity:** O(n), where n is the length of the string.  We iterate through the string twice in the worst case.
* **Space Complexity:** O(1) in the best case (e.g., string consisting of unique characters), O(n) in the worst case (e.g., all characters in string are unique).   In practice, the space used by `char_counts` is bounded by the size of the character set (e.g., 26 for lowercase English letters, or a larger number for Unicode characters). Thus it's typically O(1), treated as constant.
