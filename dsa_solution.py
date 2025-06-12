Okay, here's a random DSA problem, along with a Python solution:

**Problem:**

**First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

**Example 1:**

Input: `s = "leetcode"`
Output: `0`

**Example 2:**

Input: `s = "loveleetcode"`
Output: `2`

**Example 3:**

Input: `s = "aabb"`
Output: `-1`

**Constraints:**

*   `1 <= s.length <= 105`
*   `s` consists of only lowercase English letters.

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

    char_counts = {}  # Dictionary to store character counts

    # Count the occurrences of each character in the string
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string again to find the first character with a count of 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no non-repeating character is found, return -1
    return -1

# Example usage:
string1 = "leetcode"
print(f"First unique character in '{string1}' is at index: {firstUniqChar(string1)}")  # Output: 0

string2 = "loveleetcode"
print(f"First unique character in '{string2}' is at index: {firstUniqChar(string2)}")  # Output: 2

string3 = "aabb"
print(f"First unique character in '{string3}' is at index: {firstUniqChar(string3)}")  # Output: -1
```

**Explanation:**

1.  **Character Counting:**
    *   A dictionary `char_counts` is used to store the frequency of each character in the string `s`.
    *   The code iterates through the string `s`, and for each character, it either adds it to the dictionary with a count of 1 or increments its existing count.

2.  **Finding the First Unique Character:**
    *   The code iterates through the string `s` again, this time using `enumerate` to get both the index and the character.
    *   For each character, it checks its count in the `char_counts` dictionary.
    *   If the count is 1, it means the character is unique, so the function immediately returns its index.

3.  **Handling No Unique Characters:**
    *   If the loop completes without finding any character with a count of 1, it means there are no non-repeating characters in the string. In this case, the function returns `-1`.

**Time and Space Complexity:**

*   **Time Complexity:** O(N), where N is the length of the string `s`. The code iterates through the string twice.
*   **Space Complexity:** O(1), because at most, the `char_counts` dictionary will store the counts of all the distinct characters in the string.  Since the string consists of lowercase English letters, the dictionary can contain at most 26 entries, which is considered constant space.  So it's technically O(26), simplified to O(1).

This solution is efficient and clearly demonstrates the use of a dictionary (hash map) to solve the problem. It's also easy to understand and maintain.