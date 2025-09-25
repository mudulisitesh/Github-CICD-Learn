Okay, here's a DSA problem along with a Python solution.

**Problem:  First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

**Example:**

*   `s = "leetcode"`  Return `0`.
*   `s = "loveleetcode"` Return `2`.
*   `s = "aabb"` Return `-1`.

**Explanation:**

The goal is to efficiently find the first character that appears only once in the given string.  We need to track the frequency of each character and then find the first character with a frequency of 1.

**Python Solution:**

```python
def first_unique_char(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if no such character exists.
    """

    # Use a dictionary to store the frequency of each character.
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string again, checking for the first unique character.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1


# Example usage:
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"'{string1}': {first_unique_char(string1)}")  # Output: 'leetcode': 0
print(f"'{string2}': {first_unique_char(string2)}")  # Output: 'loveleetcode': 2
print(f"'{string3}': {first_unique_char(string3)}")  # Output: 'aabb': -1
```

**Explanation of the Code:**

1.  **Frequency Counting:**
    *   A dictionary `char_counts` is used to store the frequency of each character in the string.  The keys of the dictionary are the characters, and the values are their counts.
    *   The code iterates through the string `s`, and for each character:
        *   `char_counts[char] = char_counts.get(char, 0) + 1` increments the count of the character in the dictionary. `char_counts.get(char, 0)` efficiently handles cases where the character is seen for the first time (if it's not in the dictionary, it defaults to 0).

2.  **Finding the First Unique Character:**
    *   The code iterates through the string `s` again, this time keeping track of the index `i` of each character.
    *   For each character, it checks if its count in the `char_counts` dictionary is equal to 1.
    *   If a character has a count of 1, it means it's unique, so the function immediately returns its index `i`.

3.  **Handling No Unique Character:**
    *   If the loop completes without finding any unique characters (i.e., no character has a count of 1), the function returns -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string.  The code iterates through the string twice in the worst case.
*   **Space Complexity:** O(1), in the sense that it's bounded by the character set size. In the worst case, the dictionary `char_counts` might store counts for all the unique characters in the string.  If the character set is limited (e.g., ASCII, lowercase English letters), the space is considered constant.  If the string can contain any Unicode character, the space could technically be O(n) in the extremely unlikely worst case where every character is different.

**Alternative using `collections.Counter`:**

A slightly more concise version using `collections.Counter` is:

```python
from collections import Counter

def first_unique_char_counter(s):
    """
    Finds the index of the first non-repeating character using Counter.
    """
    char_counts = Counter(s)

    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1
```

This version achieves the same functionality but leverages the `Counter` class for simpler frequency counting.  The time and space complexity remain the same.  `Counter` is generally a good choice when you need to count the frequency of elements in a sequence.
