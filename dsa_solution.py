Okay, here's a randomly generated DSA problem and a Python solution:

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

**Constraints:**

*   `1 <= s.length <= 10^5`
*   `s` consists of only lowercase English letters.

**Python Solution**

```python
def first_uniq_char(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    # Create a dictionary to store the frequency of each character.
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string and check for the first character with a count of 1.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1

# Example usage
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"First unique character in '{string1}' is at index: {first_uniq_char(string1)}")  # Output: 0
print(f"First unique character in '{string2}' is at index: {first_uniq_char(string2)}")  # Output: 2
print(f"First unique character in '{string3}' is at index: {first_uniq_char(string3)}")  # Output: -1
```

**Explanation:**

1.  **Character Frequency Counting:**
    *   A dictionary `char_counts` is used to store the frequency (number of occurrences) of each character in the string `s`.
    *   The code iterates through the string `s`.  For each character `char`, it updates the count in the `char_counts` dictionary.  `char_counts.get(char, 0)` retrieves the current count of `char` (or 0 if it's not yet in the dictionary), and then 1 is added to it.

2.  **Finding the First Unique Character:**
    *   The code iterates through the string `s` again, this time using `enumerate` to get both the index `i` and the character `char` at each position.
    *   Inside the loop, it checks if the count of the character `char` in the `char_counts` dictionary is equal to 1.  If it is, that means the character is unique (appears only once).
    *   If a unique character is found, its index `i` is immediately returned.

3.  **Handling No Unique Characters:**
    *   If the loop completes without finding any character with a count of 1, it means there are no unique characters in the string. In this case, the function returns `-1`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  The code iterates through the string twice (once to count character frequencies and once to find the first unique character), but these are linear operations.
*   **Space Complexity:** O(1), specifically O(26), which simplifies to O(1), since we are only dealing with lowercase English alphabets. The `char_counts` dictionary will, at most, store counts for all 26 lowercase letters.  If the string could contain a larger character set (e.g., Unicode characters), the space complexity would be O(k), where k is the number of unique characters in the string.
