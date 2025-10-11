Okay, here's a randomly generated DSA problem, followed by a Python solution with explanations.

**Problem: Find the First Non-Repeating Character**

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
def first_unique_char(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    char_counts = {}  # Use a dictionary (hash map) to store character counts

    # First, count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1  # Efficiently increment count

    # Iterate through the string again to find the first non-repeating character
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i  # Return the index if the count is 1

    return -1  # No non-repeating character found

# Example Usage:
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode")) # Output: 2
print(first_unique_char("aabb"))  # Output: -1
```

**Explanation:**

1. **`char_counts = {}`:**  We initialize an empty dictionary called `char_counts`.  This dictionary will store each character in the string as a key, and its number of occurrences as the value.  Dictionaries (hash maps) provide fast lookups (O(1) on average), which is crucial for efficient character counting.

2. **Counting Character Occurrences:**

   ```python
   for char in s:
       char_counts[char] = char_counts.get(char, 0) + 1
   ```

   - The code iterates through each character `char` in the input string `s`.
   - `char_counts.get(char, 0)`: This is a concise way to get the current count of the character `char` from the `char_counts` dictionary.  If the character is already a key in the dictionary, `get()` returns its value.  If the character is not yet a key (i.e., we're encountering it for the first time), `get()` returns the default value of 0 (which we provide as the second argument).
   - `+ 1`: We increment the count by 1.
   - `char_counts[char] = ...`: We update the `char_counts` dictionary with the new count for the character.

3. **Finding the First Non-Repeating Character:**

   ```python
   for i, char in enumerate(s):
       if char_counts[char] == 1:
           return i
   ```

   - `enumerate(s)`: This allows us to iterate through the string `s` and get both the index `i` and the character `char` at each position.
   - `if char_counts[char] == 1:`:  We check the `char_counts` dictionary to see how many times the current character `char` appears in the string.  If the count is 1, it means the character is non-repeating.
   - `return i`: If we find a non-repeating character, we immediately return its index `i`.

4. **Handling No Non-Repeating Character:**

   ```python
   return -1
   ```

   - If the loop completes without finding any character with a count of 1, it means there are no non-repeating characters in the string.  In this case, the function returns -1.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the string `s`.  We iterate through the string twice, both times in linear time.
- **Space Complexity:** O(1). Although we use a dictionary, the number of distinct characters is limited by the character set (e.g., ASCII or Unicode). Therefore, the space used by the dictionary is considered constant with respect to the input string's length.  In the worst case, where all characters are unique, the dictionary will store all the characters in `s`.  However, the size is still bound by the character set, making it a constant factor.

This solution is efficient and easy to understand. The use of a dictionary allows for fast character counting, leading to the optimal O(n) time complexity.
