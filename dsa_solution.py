Okay, here's a DSA problem, along with a Python solution and explanation:

**Problem: First Unique Character in a String**

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

**Python Code Solution:**

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
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1

# Example usage:
print(first_unique_char("leetcode"))      # Output: 0
print(first_unique_char("loveleetcode"))  # Output: 2
print(first_unique_char("aabb"))          # Output: -1
```

**Explanation:**

1. **Character Counting:**
   - We create a dictionary called `char_counts` to store the frequency of each character in the string.
   - We iterate through the string `s`.
   - For each character `char`, we use `char_counts.get(char, 0) + 1` to increment its count in the dictionary.  `char_counts.get(char, 0)` returns the current count of `char` (or 0 if `char` is not yet in the dictionary), and then we add 1 to it.

2. **Finding the First Unique Character:**
   - We iterate through the string `s` again, this time keeping track of the index `i` using `enumerate()`.
   - For each character `char` at index `i`, we check its count in the `char_counts` dictionary.
   - If `char_counts[char] == 1`, it means this character appears only once in the string.  We immediately return its index `i`.

3. **Handling No Unique Character:**
   - If we iterate through the entire string without finding a unique character (i.e., no character has a count of 1), we return -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the string twice.
*   **Space Complexity:** O(1). The `char_counts` dictionary can store at most the number of unique characters in the string. In the worst case (all characters are unique), the space is proportional to the size of the character set, which is constant (e.g., 26 for lowercase English letters, or 128 for ASCII). Thus, space complexity is considered O(1). Technically O(K) where K is the number of unique characters, but K is often fixed.
**How it solves the problem:**

The core idea is to first count the frequency of each character.  Then, we iterate through the string a second time. The first character we encounter that has a count of 1 must be the first non-repeating character, so we return its index. If we get through the entire string without finding such a character, it means there are no unique characters.
