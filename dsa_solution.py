Okay, here's a DSA problem with a Python solution.

**Problem:  First Unique Character in a String**

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

**Explanation:**

The goal is to find the first character in the string that appears only once.

**Code Solution (Python):**

```python
def first_unique_char(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    # Use a dictionary to store character counts.
    char_counts = {}

    # Count the occurrences of each character.
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string and find the first character with count 1.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1

# Example usage:
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode")) # Output: 2
print(first_unique_char("aabb"))       # Output: -1
```

**Explanation of the Code:**

1. **`first_unique_char(s)` function:**
   - Takes a string `s` as input.
   - Initializes an empty dictionary `char_counts` to store the frequency of each character in the string.

2. **Counting Character Occurrences:**
   - The first `for` loop iterates through the input string `s`.
   - For each character `char`, it updates the `char_counts` dictionary:
     - `char_counts[char] = char_counts.get(char, 0) + 1`
     - `char_counts.get(char, 0)`:  This tries to get the current count of `char` from the dictionary. If `char` is not already a key in the dictionary, it returns a default value of 0.
     - `+ 1`: Increments the count by 1.  So, if the character is seen for the first time, its count becomes 1; otherwise, the existing count is incremented.

3. **Finding the First Unique Character:**
   - The second `for` loop iterates through the string `s` *again*, but this time it also gets the index `i` of each character using `enumerate()`.
   - `if char_counts[char] == 1:`:  It checks if the count of the current character `char` in the `char_counts` dictionary is equal to 1. If it is, it means the character is unique.
   - `return i`: If a unique character is found, the function immediately returns its index `i`.

4. **No Unique Character:**
   - `return -1`: If the second `for` loop completes without finding any unique characters (i.e., no character has a count of 1), the function returns -1, indicating that there are no non-repeating characters in the string.

**Time and Space Complexity:**

- **Time Complexity:** O(N), where N is the length of the string `s`.  The code iterates through the string twice (once to count frequencies and once to find the unique character).
- **Space Complexity:** O(K), where K is the number of distinct characters in the string `s`. In the worst-case scenario (all characters are distinct), K can be equal to N.  The space is used to store the character counts in the `char_counts` dictionary.  In practice, for ASCII strings, the number of distinct characters is usually much smaller than the string length.
