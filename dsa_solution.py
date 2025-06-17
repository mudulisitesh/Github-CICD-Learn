Okay, here's a DSA problem with a Python solution.

**Problem:  First Non-Repeating Character**

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
def first_unique_char(s: str) -> int:
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

    # Iterate through the string again and find the first character with count 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No non-repeating character found
# Example usage
print(first_unique_char("leetcode"))    # Output: 0
print(first_unique_char("loveleetcode")) # Output: 2
print(first_unique_char("aabb"))        # Output: -1
```

**Explanation:**

1. **`char_counts = {}`:**  We initialize an empty dictionary `char_counts` to store the frequency of each character in the string.

2. **First Loop (Counting Character Frequencies):**
   - `for char in s:`: We iterate through each character in the input string `s`.
   - `char_counts[char] = char_counts.get(char, 0) + 1`:  For each character `char`, we update its count in the `char_counts` dictionary. `char_counts.get(char, 0)` retrieves the current count of `char`.  If `char` is not already in the dictionary, `get()` returns 0 (the default value). We then increment the count by 1.

3. **Second Loop (Finding the First Unique Character):**
   - `for i, char in enumerate(s):`: We iterate through the string `s` again, this time using `enumerate()` to get both the index `i` and the character `char` at each position.
   - `if char_counts[char] == 1:`: We check if the count of the current character `char` in the `char_counts` dictionary is equal to 1.  If it is, it means the character appears only once in the string.
   - `return i`: If we find a character with a count of 1, we immediately return its index `i`.

4. **`return -1`:**  If the loop completes without finding any character with a count of 1, it means there are no non-repeating characters in the string. In this case, we return -1.

**Time and Space Complexity:**

* **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the string twice.
* **Space Complexity:** O(1).  In the worst case, the `char_counts` dictionary will store the counts for all unique characters in the string. However, since we are dealing with characters (typically ASCII or Unicode), the number of unique characters is bounded by a constant (e.g., 128 for ASCII, potentially larger but still bounded for Unicode). Therefore, the space complexity is considered constant.
