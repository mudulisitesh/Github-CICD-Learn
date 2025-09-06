Okay, here's a DSA problem, along with a Python solution:

**Problem: First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example:**

```
s = "leetcode"
Output: 0  (because 'l' is the first unique character)

s = "loveleetcode"
Output: 2  (because 'v' is the first unique character)

s = "aabb"
Output: -1  (no unique character exists)
```

**Solution in Python:**

```python
def first_unique_character(s: str) -> int:
    """
    Finds the index of the first unique character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    char_counts = {}  # Dictionary to store character counts

    # Count character frequencies
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find the first character with a count of 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No unique character found


# Example usage:
s1 = "leetcode"
print(f"First unique character in '{s1}': {first_unique_character(s1)}")  # Output: 0

s2 = "loveleetcode"
print(f"First unique character in '{s2}': {first_unique_character(s2)}")  # Output: 2

s3 = "aabb"
print(f"First unique character in '{s3}': {first_unique_character(s3)}")  # Output: -1

s4 = "dddccdbba"
print(f"First unique character in '{s4}': {first_unique_character(s4)}") # Output: 8
```

**Explanation:**

1. **Character Counting:**
   - We use a dictionary `char_counts` to store the frequency of each character in the input string `s`.
   - We iterate through the string, updating the count for each character.  `char_counts.get(char, 0) + 1` elegantly handles the case where a character is seen for the first time (the default value `0` is returned by `get` in that case).

2. **Finding the First Unique Character:**
   - We iterate through the string `s` *again*, this time also keeping track of the index `i` using `enumerate`.
   - For each character `char`, we check its count in the `char_counts` dictionary.
   - If the count is 1 (meaning it's a unique character), we immediately return its index `i`.

3. **No Unique Character:**
   - If the loop completes without finding a character with a count of 1, it means there are no unique characters in the string. In this case, we return -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the string twice (once to count characters, and once to find the first unique one).
*   **Space Complexity:** O(1) in the sense that it is bounded by a constant number of possible ASCII characters (128) or extended ASCII characters (256).  In practice, it could be considered O(N) in the worst case if the string contains N unique characters. The dictionary stores at most the count of each unique character.  So it scales with the number of unique characters, not necessarily the total length of the string.

**Key Concepts Used:**

*   **Dictionaries (Hash Maps):**  Dictionaries are essential for efficiently storing and retrieving the counts of characters.
*   **Iteration:**  Iterating through the string using a `for` loop and `enumerate` is crucial for accessing both the characters and their indices.
*   **Frequency Counting:** This is a common pattern in many string problems, where you need to analyze the frequencies of characters or elements.
