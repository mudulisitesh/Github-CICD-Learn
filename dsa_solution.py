Okay, here's a DSA problem with a Python solution:

**Problem: First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example:**

*   **Input:** `s = "leetcode"`
*   **Output:** `0`

*   **Input:** `s = "loveleetcode"`
*   **Output:** `2`

*   **Input:** `s = "aabb"`
*   **Output:** `-1`

**Explanation:**

The first non-repeating character in "leetcode" is 'l' at index 0.
The first non-repeating character in "loveleetcode" is 'v' at index 2.
All characters in "aabb" repeat.

**Python Solution:**

```python
def first_unique_char(s: str) -> int:
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

    # No unique character found
    return -1

# Example usage
print(first_unique_char("leetcode"))    # Output: 0
print(first_unique_char("loveleetcode")) # Output: 2
print(first_unique_char("aabb"))       # Output: -1
```

**Explanation of the Code:**

1.  **Character Counting:**
    *   We use a dictionary `char_counts` to store the number of times each character appears in the string.  We iterate through the string and update the counts. `char_counts.get(char, 0)` is used to retrieve the current count of the character `char`. If `char` is not already in `char_counts`, it returns 0 as the default value.  We then add 1 to the count.

2.  **Finding the First Unique Character:**
    *   We iterate through the string again, this time keeping track of the index `i` of each character.
    *   For each character, we check if its count in `char_counts` is equal to 1. If it is, it means the character appears only once in the string, and we return its index `i`.

3.  **Handling No Unique Characters:**
    *   If the loop completes without finding any character with a count of 1, it means there are no unique characters in the string. In this case, we return -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(N), where N is the length of the string.  We iterate through the string twice in the worst case.
*   **Space Complexity:** O(1). The `char_counts` dictionary can store at most 26 unique characters (for lowercase English alphabets), or a constant number of characters based on the character set of the input string. Hence the space complexity is considered constant.  In the worst case, all characters in the input string are unique, so the dictionary would store all those characters. But practically it's considered O(1) for typical character sets. If we considered all possible Unicode characters, then the space complexity could technically approach O(N), but for most practical cases (ASCII, common Unicode character sets), we can reasonably treat it as constant.
