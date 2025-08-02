Okay, here's a random DSA problem and a Python solution:

**Problem:  First Unique Character in a String**

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

**Solution (Python):**

```python
def first_unique_char(s: str) -> int:
    """
    Finds the index of the first unique character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    char_counts = {}  # Dictionary to store character counts
    n = len(s)

    # First pass: Count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Second pass: Find the first character with a count of 1
    for i in range(n):
        if char_counts[s[i]] == 1:
            return i

    return -1  # No unique character found

# Example Usage
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"'{string1}': {first_unique_char(string1)}")  # Output: 0
print(f"'{string2}': {first_unique_char(string2)}")  # Output: 2
print(f"'{string3}': {first_unique_char(string3)}")  # Output: -1
```

**Explanation:**

1. **`first_unique_char(s: str) -> int:`**
   - This defines the function signature, indicating that it takes a string `s` as input and returns an integer (the index or -1).

2. **`char_counts = {}`**
   - A dictionary `char_counts` is initialized to store the counts of each character in the string.

3. **`n = len(s)`**
   - The length of the string is stored in `n` for efficiency.

4. **First Pass (Character Counting):**
   ```python
   for char in s:
       char_counts[char] = char_counts.get(char, 0) + 1
   ```
   - This loop iterates through each character `char` in the string `s`.
   - `char_counts.get(char, 0)`: This attempts to retrieve the current count of the character `char` from the `char_counts` dictionary.  If the character is not yet in the dictionary (it's the first time we've seen it), `get()` returns a default value of 0.
   - `+ 1`:  We increment the count (either the existing count or the initial 0).
   - `char_counts[char] = ...`:  The updated count is stored back into the `char_counts` dictionary for that character.

5. **Second Pass (Finding the First Unique Character):**
   ```python
   for i in range(n):
       if char_counts[s[i]] == 1:
           return i
   ```
   - This loop iterates through the string again, but this time using indices `i` from 0 to `n - 1`.
   - `s[i]`: This accesses the character at the current index `i`.
   - `char_counts[s[i]] == 1`:  This checks if the count of the character at the current index is equal to 1.  If it is, it means that this character is unique.
   - `return i`: If a unique character is found, the function immediately returns its index `i`.

6. **`return -1`**
   - If the loop completes without finding any character with a count of 1, it means that there are no unique characters in the string, so the function returns -1.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the string.  We iterate through the string twice (once to count characters and once to find the first unique character).
- **Space Complexity:** O(1).  In the worst case, the `char_counts` dictionary will store counts for all the unique characters in the string. However, since we are dealing with ASCII characters (or a limited character set), the size of the dictionary is bounded by a constant (e.g., 128 or 256 for ASCII/extended ASCII).  Therefore, we can consider the space complexity to be O(1).  If we had to deal with arbitrary Unicode characters, it would be O(k) where k is the number of unique characters in the string. However, because the number of unique characters is fixed (e.g., 256 for ASCII), we call it O(1).
