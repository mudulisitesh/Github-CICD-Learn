Okay, here's a random DSA problem, along with a Python solution and explanation:

**Problem:**

**First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

**Example:**

*   Input: `s = "leetcode"`
*   Output: `0` (The first unique character is 'l' at index 0.)

*   Input: `s = "loveleetcode"`
*   Output: `2` (The first unique character is 'v' at index 2.)

*   Input: `s = "aabb"`
*   Output: `-1` (There are no unique characters.)

**Solution (Python):**

```python
def firstUniqChar(s):
    """
    Finds the index of the first unique character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    # Create a dictionary to store character frequencies.
    char_counts = {}

    # Count the occurrences of each character.
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string again to find the first unique character.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1

# Test cases:
print(firstUniqChar("leetcode"))    # Output: 0
print(firstUniqChar("loveleetcode")) # Output: 2
print(firstUniqChar("aabb"))      # Output: -1
```

**Explanation:**

1.  **Frequency Counting:**

    *   We use a dictionary `char_counts` to store the frequency of each character in the string.
    *   The first loop iterates through the string `s`.
    *   For each character, we update its count in the `char_counts` dictionary.  `char_counts.get(char, 0)` efficiently retrieves the current count of the character.  If the character is not already in the dictionary, `get()` returns 0 (the default value), so we start the count at 0 if it's the first time we see the character.  We then increment the count by 1.

2.  **Finding the First Unique Character:**

    *   The second loop iterates through the string `s` again, but this time, we also have access to the index `i` of each character.
    *   For each character, we check if its count in `char_counts` is equal to 1.  If it is, it means the character is unique.
    *   We immediately return the index `i` of the first unique character we find.

3.  **No Unique Character:**

    *   If the second loop completes without finding any unique characters (i.e., no character has a count of 1), we return `-1`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`. We iterate through the string twice (once for counting frequencies and once for finding the unique character).
*   **Space Complexity:** O(1).  In the worst case, the `char_counts` dictionary will store the frequency of all unique characters in the string. However, the number of unique characters is limited to the size of the alphabet (26 for lowercase English letters). Therefore, the space complexity is considered constant. In a more general scenario with Unicode characters, the space complexity could be considered O(k) where k is the number of unique characters.  However, since k is still bounded by the character set size, it can often be treated as a constant.
