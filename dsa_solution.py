Okay, here's a randomly generated DSA problem, along with a Python solution:

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
def firstUniqChar(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    # Create a dictionary to store the frequency of each character.
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string again.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1

# Example Usage:
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"First unique character index in '{string1}': {firstUniqChar(string1)}")  # Output: 0
print(f"First unique character index in '{string2}': {firstUniqChar(string2)}")  # Output: 2
print(f"First unique character index in '{string3}': {firstUniqChar(string3)}")  # Output: -1
```

**Explanation:**

1. **Character Counting:**
   - We use a dictionary `char_counts` to store the frequency of each character in the input string `s`.
   - We iterate through the string, and for each character, we increment its count in the dictionary.  `char_counts.get(char, 0)` is used to safely handle cases where the character is encountered for the first time (if it's not in the dictionary yet, it returns 0 as the default value).

2. **Finding the First Unique Character:**
   - We iterate through the string `s` *again*, along with its index `i` using `enumerate`.
   - For each character, we check its count in the `char_counts` dictionary.
   - If the count is equal to 1, it means that the character is unique (appears only once in the string).  In that case, we immediately return its index `i`.

3. **No Unique Character Found:**
   - If the loop completes without finding a unique character (i.e., no character has a count of 1), we return -1 to indicate that there is no first unique character in the string.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the string `s`.  We iterate through the string twice.
- **Space Complexity:** O(1).  The space used by the `char_counts` dictionary is limited to the number of unique characters in the string. In the worst case (all characters are unique), the space complexity is O(n). However, since we're dealing with ASCII characters (typically 128 or 256 characters), the dictionary's size is bounded by a constant, making it effectively O(1).
