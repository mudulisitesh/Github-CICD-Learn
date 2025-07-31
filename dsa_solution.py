Okay, here's a random DSA problem, followed by a Python solution.

**Problem: First Unique Character in a String**

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

    # Count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find the first character with count 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No unique character found
# Example Usage:
s1 = "leetcode"
print(f"First unique char in '{s1}': {firstUniqChar(s1)}")  # Output: 0

s2 = "loveleetcode"
print(f"First unique char in '{s2}': {firstUniqChar(s2)}")  # Output: 2

s3 = "aabb"
print(f"First unique char in '{s3}': {firstUniqChar(s3)}")  # Output: -1

s4 = ""
print(f"First unique char in '{s4}': {firstUniqChar(s4)}") # Output: -1

s5 = "abcabcbb"
print(f"First unique char in '{s5}': {firstUniqChar(s5)}") # Output: -1

s6 = "a"
print(f"First unique char in '{s6}': {firstUniqChar(s6)}") # Output: 0

s7 = "adaadcb"
print(f"First unique char in '{s7}': {firstUniqChar(s7)}") # Output: 6
```

**Explanation:**

1. **Character Counts:**  A dictionary `char_counts` is used to store the frequency of each character in the string. The `.get(char, 0)` method efficiently retrieves the current count (or defaults to 0 if the character hasn't been seen yet) and increments it.

2. **First Unique Character:** The code then iterates through the string `s` *again*.  This time, it checks the count of each character using the `char_counts` dictionary. If a character's count is equal to 1, it means the character appears only once, so the function immediately returns its index `i`.

3. **No Unique Character:** If the loop completes without finding any character with a count of 1, the function returns `-1`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`. We iterate through the string twice in the worst case.
*   **Space Complexity:** O(1). Although we use a dictionary, in the worst case, it will store at most 26 characters (for lowercase English letters). So it's considered constant space with respect to the length of the input string (because the maximum size of the dictionary doesn't depend on the size of the string, assuming the string only contains ASCII characters). If the input string can contain any Unicode character, then the space complexity is O(number of unique characters in the input string), which could be up to O(n) in some cases.  However, in practice, the number of unique characters is often much smaller than `n`. Using a fixed-size array of size 256 (assuming extended ASCII) could also be an option for constant space if the character set is limited.

**Alternative Solution (using collections.Counter):**

```python
from collections import Counter

def firstUniqChar_counter(s):
    """
    Finds the index of the first non-repeating character using collections.Counter.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    char_counts = Counter(s)

    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1
```

This alternative is more concise because `collections.Counter` does the character counting automatically.  The time and space complexity are the same as the first solution.  It's generally preferred for its readability.
