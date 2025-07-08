Okay, here's a randomly generated DSA problem, followed by a Python solution with explanations.

**Problem:  Find the First Non-Repeating Character**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example 1:**

Input: s = "leetcode"
Output: 0

**Example 2:**

Input: s = "loveleetcode"
Output: 2

**Example 3:**

Input: s = "aabb"
Output: -1

**Constraints:**

*   `1 <= s.length <= 10^5`
*   `s` consists of lowercase English letters.

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
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string to find the first character with count 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No non-repeating character found


# Example Usage:
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"'{string1}': {first_unique_char(string1)}")  # Output: 0
print(f"'{string2}': {first_unique_char(string2)}")  # Output: 2
print(f"'{string3}': {first_unique_char(string3)}")  # Output: -1
```

**Explanation:**

1.  **Character Counting:**
    *   We use a dictionary `char_counts` to store the frequency of each character in the string `s`.
    *   We iterate through the string, and for each character:
        *   If the character is already in the dictionary, we increment its count.
        *   If the character is not in the dictionary, we add it with a count of 1.  `char_counts.get(char, 0)` is a concise way to either retrieve the existing count or default to 0 if it's the first time we've seen the character.

2.  **Finding the First Unique:**
    *   After counting the characters, we iterate through the string `s` again, this time keeping track of the index `i`.
    *   For each character at index `i`, we check its count in the `char_counts` dictionary.
    *   If the count is 1, it means the character is non-repeating. We immediately return the index `i`.

3.  **No Unique Character:**
    *   If we complete the second loop without finding any character with a count of 1, it means there are no non-repeating characters in the string.  In this case, we return -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the string twice.
*   **Space Complexity:** O(1). In the worst case, the dictionary `char_counts` will store the count of all unique characters in the string. Since the string consists of lowercase English letters, the maximum number of unique characters is 26, making the space complexity constant.  We can say O(26) which simplifies to O(1). If it was Unicode, it would be O(U) where U is the number of unique Unicode characters, potentially much larger.

**Why this approach is good:**

*   **Clarity:** The code is relatively straightforward and easy to understand.
*   **Efficiency:**  It avoids nested loops, resulting in a linear time complexity.
*   **Readability:**  Using a dictionary to store counts is a common and well-understood approach for this type of problem.

This is a common and important type of string problem that often appears in coding interviews.  Understanding the frequency counting approach and how to efficiently iterate through the string is key to solving this and similar problems.
