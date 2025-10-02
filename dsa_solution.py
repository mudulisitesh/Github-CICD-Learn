Okay, here's a DSA problem and its Python solution:

**Problem:**

**First Unique Character in a String**

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

**Constraints:**

*   `1 <= s.length <= 10^5`
*   `s` consists of lowercase English letters.

**Solution (Python):**

```python
def firstUniqChar(s: str) -> int:
    """
    Finds the index of the first unique character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    # Create a dictionary to store character counts.
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string and check the counts.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1

# Example Usage:
s1 = "leetcode"
print(f"'{s1}': {firstUniqChar(s1)}")  # Output: 0

s2 = "loveleetcode"
print(f"'{s2}': {firstUniqChar(s2)}")  # Output: 2

s3 = "aabb"
print(f"'{s3}': {firstUniqChar(s3)}")  # Output: -1

s4 = "dddccdbba"
print(f"'{s4}': {firstUniqChar(s4)}") # Output: 8
```

**Explanation:**

1.  **Character Counting (Hash Map):**
    *   A dictionary `char_counts` is used to store the frequency of each character in the input string `s`.
    *   The code iterates through the string and updates the count of each character in the dictionary. `char_counts.get(char, 0)` safely retrieves the current count of the character (or 0 if it's not yet in the dictionary) and then increments it by 1.

2.  **Finding the First Unique Character:**
    *   The code iterates through the string again, this time keeping track of the index `i` of each character.
    *   For each character, it checks its count in the `char_counts` dictionary.
    *   If the count is equal to 1, it means the character is unique. In this case, the function immediately returns the index `i`.

3.  **Handling No Unique Character:**
    *   If the loop completes without finding any character with a count of 1, it means there are no unique characters in the string. In this case, the function returns -1.

**Time Complexity:**

*   O(n), where n is the length of the string `s`.  The code iterates through the string twice.  The dictionary operations (get and set) take O(1) on average.

**Space Complexity:**

*   O(1). Because the string contains only lowercase English letters, the dictionary `char_counts` can store at most 26 entries.  Therefore, the space used is constant.  We can say it's O(n) in the worst-case scenario that all n chars are unique. But in practice, if we know the character set is small, it's often regarded as O(1).
