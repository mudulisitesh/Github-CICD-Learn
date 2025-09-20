Okay, here's a randomly generated DSA problem and its Python solution:

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
        The index of the first unique character, or -1 if none exists.
    """

    char_counts = {}  # Dictionary to store character counts

    # Count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string again to find the first unique character
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No unique character found
# Example Usage:
string1 = "leetcode"
print(f"First unique character in '{string1}' is at index: {firstUniqChar(string1)}") # Output: 0

string2 = "loveleetcode"
print(f"First unique character in '{string2}' is at index: {firstUniqChar(string2)}") # Output: 2

string3 = "aabb"
print(f"First unique character in '{string3}' is at index: {firstUniqChar(string3)}") # Output: -1
```

**Explanation:**

1. **Character Counting:**
   - We use a dictionary `char_counts` to store the frequency of each character in the string.
   - We iterate through the string `s`, and for each character `char`, we increment its count in the `char_counts` dictionary.  The `.get(char, 0)` method handles the case where the character is encountered for the first time (it defaults the count to 0).

2. **Finding the First Unique:**
   - We iterate through the string `s` again, this time along with its index `i`.
   - For each character `char`, we check if its count in `char_counts` is equal to 1. If it is, it means the character is unique.
   - If we find a unique character, we immediately return its index `i`.

3. **No Unique Character:**
   - If we iterate through the entire string and don't find any unique characters, we return -1.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the string `s`.  We iterate through the string twice.
- **Space Complexity:** O(1). In the worst case, the `char_counts` dictionary will store the counts of all unique characters in the string.  The size of the dictionary is bounded by the size of the character set (e.g., 26 for lowercase English letters, 128 for ASCII). So, we can consider it as constant space.
