Okay, here's a DSA problem and a Python solution:

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

**Python Solution:**

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

    # If no non-repeating character is found
    return -1

# Example Usage:
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"First unique char in '{string1}': {firstUniqChar(string1)}")
print(f"First unique char in '{string2}': {firstUniqChar(string2)}")
print(f"First unique char in '{string3}': {firstUniqChar(string3)}")
```

**Explanation:**

1. **Character Counting:**
   - A dictionary `char_counts` is used to store the frequency of each character in the input string `s`.
   - The code iterates through the string, and for each character, it either increments its count in the dictionary (if it's already present) or adds it to the dictionary with a count of 1 (if it's the first time encountering the character).  `char_counts.get(char, 0)` is a concise way to handle both cases.  If `char` is already a key in `char_counts`, `char_counts.get(char, 0)` returns the existing value; otherwise, it returns 0 (the default value), ensuring that new characters start with a count of zero.

2. **Finding the First Unique Character:**
   - The code iterates through the string `s` again, this time along with its index `i` using `enumerate(s)`.
   - For each character `char` at index `i`, it checks if `char_counts[char]` is equal to 1. If it is, it means that this character appears only once in the string.
   - If a unique character is found, its index `i` is immediately returned.

3. **No Unique Character Found:**
   - If the loop completes without finding any character with a count of 1, it means that there are no non-repeating characters in the string. In this case, the function returns -1.

**Time and Space Complexity:**

- **Time Complexity:** O(N), where N is the length of the string `s`.  We iterate through the string twice.
- **Space Complexity:** O(1) in the sense that, at worst, the `char_counts` dictionary will store the count of each *unique* character in the string. Since the number of unique characters in a string is limited (e.g., 26 for lowercase English letters), the space used by the dictionary remains relatively constant regardless of the length of the input string.  Technically, it's O(k) where k is the size of the alphabet, which is usually considered a constant for practical purposes.

**How to run the code:**

1.  **Save:** Save the code as a `.py` file (e.g., `unique_char.py`).
2.  **Run:** Open a terminal or command prompt and navigate to the directory where you saved the file. Then, run the script using the command: `python unique_char.py`

The output will show the results for the three example strings.
