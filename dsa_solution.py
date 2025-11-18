Okay, here's a random DSA problem with a Python solution:

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

**Solution (Python):**

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

    # Count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find the first character with a count of 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No unique character found

# Example usage:
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"'{string1}': {firstUniqChar(string1)}")  # Output: 0
print(f"'{string2}': {firstUniqChar(string2)}")  # Output: 2
print(f"'{string3}': {firstUniqChar(string3)}")  # Output: -1
```

**Explanation:**

1. **`char_counts = {}`**:  We initialize an empty dictionary called `char_counts`. This dictionary will store each character in the string as a key and the number of times it appears in the string as the value.

2. **`for char in s:`**:  We iterate through the input string `s` character by character.

3. **`char_counts[char] = char_counts.get(char, 0) + 1`**:  For each character `char`, we update its count in the `char_counts` dictionary.  `char_counts.get(char, 0)` retrieves the current count of `char` from the dictionary.  If `char` is not already in the dictionary, `get(char, 0)` returns 0 (the default value), meaning it's the first time we've seen this character.  Then, we add 1 to the current count and store it back in the dictionary.

4. **`for i, char in enumerate(s):`**:  We iterate through the string `s` again, this time using `enumerate` to get both the index `i` and the character `char` at that index.

5. **`if char_counts[char] == 1:`**:  Inside the loop, we check if the count of the current character `char` in the `char_counts` dictionary is equal to 1. If it is, this means the character appears only once in the string.

6. **`return i`**:  If we find a character with a count of 1, we immediately return its index `i`.

7. **`return -1`**:  If the loop completes without finding any characters with a count of 1, it means there are no unique characters in the string. In this case, we return -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`. We iterate through the string twice in the worst case.
*   **Space Complexity:** O(1). In the worst case, the `char_counts` dictionary can store up to 26 key-value pairs (for lowercase English letters). The space complexity is therefore constant, independent of the string's length.  While it technically could be O(k) where k is the size of the character set (e.g., ASCII, Unicode), it's usually considered O(1) because `k` is a fixed constant.
