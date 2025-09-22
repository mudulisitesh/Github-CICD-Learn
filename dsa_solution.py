Okay, here's a random DSA problem and a corresponding Python solution:

**Problem: First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

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

**Conceptual Explanation**

The core idea is to:

1.  **Count Character Frequencies:**  Go through the string and keep track of how many times each character appears.  A dictionary (hash map) is perfect for this.
2.  **Find the First Unique:** Iterate through the string *again*.  This time, for each character, look up its frequency in the dictionary.  If the frequency is 1, that's your first unique character. Return its index.
3.  **Handle No Unique Character:** If the loop finishes without finding any character with a frequency of 1, it means there's no unique character.  Return -1.

**Python Code Solution**

```python
def first_unique_char(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    char_counts = {}  # Dictionary to store character frequencies

    # First pass: Count character frequencies
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Second pass: Find the first character with frequency 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No unique character found

# Example Usage
print(first_unique_char("leetcode"))    # Output: 0
print(first_unique_char("loveleetcode")) # Output: 2
print(first_unique_char("aabb"))         # Output: -1
```

**Explanation of the Code:**

1.  **`first_unique_char(s)` Function:**
    *   Takes the input string `s` as an argument.
    *   Initializes an empty dictionary `char_counts` to store character frequencies.

2.  **First Pass (Frequency Counting):**
    *   `for char in s:`: Iterates through each character in the string.
    *   `char_counts[char] = char_counts.get(char, 0) + 1`: This line updates the frequency count for the current character `char`.
        *   `char_counts.get(char, 0)`:  This tries to get the current count of `char` from the dictionary. If `char` is not yet in the dictionary (first time seeing it), it returns 0 as the default value.
        *   `+ 1`: Increments the count.
        *   `char_counts[char] = ...`:  Assigns the updated count back to the `char` key in the dictionary.

3.  **Second Pass (Finding First Unique):**
    *   `for i, char in enumerate(s):`: Iterates through the string *again*, this time using `enumerate` to get both the index `i` and the character `char` at each position.
    *   `if char_counts[char] == 1:`:  Checks if the frequency of the current character (looked up in the `char_counts` dictionary) is equal to 1.  If it is, it means this is a unique character.
    *   `return i`:  Immediately returns the index `i` of the first unique character.

4.  **No Unique Character:**
    *   `return -1`: If the loop completes without finding any character with a frequency of 1, it means there are no unique characters in the string.  The function returns -1 to indicate this.

**Time and Space Complexity**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  We iterate through the string twice in the worst case.
*   **Space Complexity:** O(1). In the worst case, the `char_counts` dictionary will store all the distinct characters in the string. However, the size of the dictionary is limited by the size of the character set (e.g., for ASCII characters, it's at most 128; for Unicode, it's larger, but still constant relative to the input string's arbitrary length).  Therefore, the space is considered O(1).

**Key Improvements and Considerations**

*   **Clarity:** The code is written to be readable and easy to understand.
*   **Efficiency:** The use of a dictionary provides efficient lookups (average O(1) time).
*   **Edge Cases:**  The code handles the case where there are no unique characters by returning -1.
*   **Character Set:**  If you were dealing with a very large character set (e.g., extended Unicode), you might consider using a more space-efficient data structure if memory usage becomes a concern, but for common cases, the dictionary is the most practical and clear approach.
