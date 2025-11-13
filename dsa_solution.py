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
def firstUniqChar(s: str) -> int:
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    # Create a dictionary to store the frequency of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string and check if the character's count is 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1
    return -1

# Example usage:
print(firstUniqChar("leetcode"))  # Output: 0
print(firstUniqChar("loveleetcode")) # Output: 2
print(firstUniqChar("aabb"))       # Output: -1
```

**Explanation:**

1. **Frequency Counting:**
   - We use a dictionary `char_counts` to store the frequency of each character in the string.
   - We iterate through the string `s` and update the count for each character.  `char_counts.get(char, 0) + 1` safely increments the count, initializing it to 0 if the character is not yet in the dictionary.

2. **Finding the First Unique:**
   - We iterate through the string `s` again, this time keeping track of the index `i`.
   - For each character, we check its count in the `char_counts` dictionary.
   - If the count is 1, it means the character is unique. We return its index `i`.

3. **No Unique Character:**
   - If we reach the end of the string without finding a unique character, it means there are no non-repeating characters. In this case, we return -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  We iterate through the string twice.
*   **Space Complexity:** O(1).  In the worst case, the `char_counts` dictionary will store counts for all unique characters in the string. However, since the string consists of characters, and the number of possible ASCII characters is limited (e.g., 128 or 256), the space used by the dictionary is bounded by a constant.  Therefore, we consider it O(1).
