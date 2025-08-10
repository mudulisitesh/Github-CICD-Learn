Okay, here's a random DSA problem and a Python solution:

**Problem:  First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

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

**Python Code Solution:**

```python
def firstUniqChar(s: str) -> int:
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    char_counts = {}  # Dictionary to store character counts
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1

# Example Usage:
print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
```

**Explanation:**

1. **Character Counting:**
   - We use a dictionary `char_counts` to store the frequency of each character in the string. We iterate through the string `s`.
   - For each character, we increment its count in the `char_counts` dictionary.  The `char_counts.get(char, 0)` part elegantly handles characters not yet encountered. If `char` is not in the dictionary, `get()` returns 0, otherwise it returns the current count.

2. **Finding the First Unique Character:**
   - After counting the characters, we iterate through the string `s` *again* using `enumerate` to get both the index (`i`) and the character (`char`).
   - For each character, we check its count in the `char_counts` dictionary.
   - If the count is equal to 1, it means the character appears only once in the string.  We immediately return the index `i`.

3. **Handling No Unique Characters:**
   - If the loop completes without finding any character with a count of 1, it means there are no unique characters in the string.  In this case, we return -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  We iterate through the string twice (once for counting and once for finding the unique character).
*   **Space Complexity:** O(1). In the worst case, the dictionary `char_counts` could store the counts of all unique characters in the string. But since there are a limited number of characters (e.g., ASCII characters), the space used by the dictionary is effectively constant.  For a string using only lowercase English letters, the maximum size of `char_counts` is 26.

**Why this is a good DSA problem:**

*   **Common Task:** Finding unique elements is a frequently encountered sub-problem in various coding scenarios.
*   **Data Structures:** It effectively utilizes a dictionary (hash map) for efficient counting and lookup.  Dictionaries are a fundamental data structure.
*   **Algorithm:** It showcases a two-pass approach, which is a common algorithmic pattern.  The first pass prepares data (character counts), and the second pass uses that data to find the desired result.
*   **Clear Requirements:** The problem statement is concise and unambiguous.
*   **Scalability:** The solution has a linear time complexity, making it suitable for moderately large input strings.
