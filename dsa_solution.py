Okay, here's a DSA problem along with a Python solution:

**Problem:  First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example 1:**

Input: `s = "leetcode"`
Output: 0

**Example 2:**

Input: `s = "loveleetcode"`
Output: 2

**Example 3:**

Input: `s = "aabb"`
Output: -1

**Constraints:**

*   `1 <= s.length <= 10^5`
*   `s` consists of lowercase English letters.

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

    char_counts = {}  # Dictionary to store character counts

    # Count character occurrences
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find the first character with a count of 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No unique character found

# Example Usage:
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"First unique char in '{string1}': {firstUniqChar(string1)}")
print(f"First unique char in '{string2}': {firstUniqChar(string2)}")
print(f"First unique char in '{string3}': {firstUniqChar(string3)}")
```

**Explanation:**

1.  **Character Counting:**
    *   We create a dictionary `char_counts` to store the frequency of each character in the string.
    *   We iterate through the string `s`, and for each character `char`, we increment its count in the `char_counts` dictionary.  `char_counts.get(char, 0)` elegantly handles cases where a character is seen for the first time; it returns 0 if `char` isn't already a key, and then we add 1.

2.  **Finding the First Unique Character:**
    *   We iterate through the string `s` again, this time using `enumerate` to get both the index (`i`) and the character (`char`) at that index.
    *   For each character, we check its count in the `char_counts` dictionary.  If the count is 1, it means the character is unique.
    *   If we find a character with a count of 1, we immediately return its index `i`.

3.  **No Unique Character:**
    *   If we complete the loop without finding a unique character, it means there are no non-repeating characters in the string.  In this case, we return -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string.  We iterate through the string twice in the worst case.
*   **Space Complexity:** O(1). Although we use a dictionary, the size of the dictionary is limited by the number of unique characters in the alphabet (26 for lowercase English letters), which is constant. So it effectively becomes O(1).   In cases where you have non-ascii characters, this is technically O(k) where k is the size of your character set, but still considered a small constant for many applications.
