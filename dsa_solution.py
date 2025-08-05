Okay, here's a DSA problem and a Python solution.

**Problem:  Find the First Non-Repeating Character**

Given a string, find the first non-repeating character in it.  If it does not exist, return None.

**Example:**

*   `string = "leetcode"`  Output: `l`
*   `string = "loveleetcode"` Output: `v`
*   `string = "aabbcc"` Output: `None`

**Explanation:**

The goal is to identify the character that appears only once in the string and is also the earliest one that does so. We can use a hash map (dictionary in Python) to store character counts and then iterate through the string again to find the first character with a count of 1.

**Python Code:**

```python
def first_non_repeating_char(s):
    """
    Finds the first non-repeating character in a string.

    Args:
      s: The input string.

    Returns:
      The first non-repeating character, or None if it doesn't exist.
    """

    char_counts = {}  # Use a dictionary to store character counts

    # Count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find the first character with a count of 1
    for char in s:
        if char_counts[char] == 1:
            return char

    # If no non-repeating character is found, return None
    return None

# Example usage
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabbcc"

print(f"First non-repeating char in '{string1}': {first_non_repeating_char(string1)}") # Output: l
print(f"First non-repeating char in '{string2}': {first_non_repeating_char(string2)}") # Output: v
print(f"First non-repeating char in '{string3}': {first_non_repeating_char(string3)}") # Output: None
```

**Explanation of the Code:**

1.  **`first_non_repeating_char(s)` Function:**
    *   Takes the input string `s` as an argument.
    *   Initializes an empty dictionary called `char_counts`. This dictionary will store the count of each character in the string.

2.  **Counting Character Occurrences:**
    *   The code iterates through each character `char` in the string `s`.
    *   For each character, it updates the `char_counts` dictionary.
        *   `char_counts.get(char, 0)`: This tries to get the current count of the character `char` from the dictionary. If the character is not already in the dictionary (i.e., it's the first time we've seen it), `get()` returns a default value of 0.
        *   `+ 1`: We increment the count by 1.
        *   `char_counts[char] = ...`: We store the updated count back into the `char_counts` dictionary for the character `char`.

3.  **Finding the First Non-Repeating Character:**
    *   The code iterates through the string `s` *again*. This is necessary to maintain the original order of characters in the string.
    *   For each character `char` in the string, it checks if `char_counts[char] == 1`.  This means the character only appears once in the string.
    *   If a character with a count of 1 is found, the function immediately returns that character.  This ensures we return the *first* non-repeating character.

4.  **Handling the Case of No Non-Repeating Character:**
    *   If the loop completes without finding any character with a count of 1, it means there are no non-repeating characters in the string.
    *   In this case, the function returns `None`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string.  We iterate through the string twice, but each iteration is linear.
*   **Space Complexity:** O(1).  In the worst case, the `char_counts` dictionary will store all unique characters in the string. In most character sets (e.g., ASCII), the number of unique characters is limited to a constant (like 128 or 256), so the space complexity is considered O(1) or constant.  In theory, if the input string used a truly unbounded unicode character set, it could approach O(n) but that's very unlikely in practical use cases.  In practice, O(1) is more accurate.
