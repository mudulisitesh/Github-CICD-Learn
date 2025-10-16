Okay, here's a random DSA problem and a Python solution:

**Problem:**

**Find the First Non-Repeating Character in a String**

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

    char_counts = {}  # Use a dictionary to store character counts

    # Count the occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string again to find the first character with a count of 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1  # No non-repeating character found
#Test Cases:
print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
```

**Explanation:**

1.  **`char_counts = {}`:** We initialize an empty dictionary called `char_counts`. This dictionary will store each character in the string `s` as a key, and the number of times that character appears in the string as its value.

2.  **First Loop (Counting Occurrences):**
    *   `for char in s:`: We iterate through each character in the input string `s`.
    *   `char_counts[char] = char_counts.get(char, 0) + 1`:  This is the core of the counting logic:
        *   `char_counts.get(char, 0)`: We try to retrieve the current count of the character `char` from the `char_counts` dictionary.  If the character is *not* already a key in the dictionary (i.e., it's the first time we've seen this character), `get(char, 0)` returns 0 (the default value).
        *   `+ 1`:  We add 1 to the current count (either the existing count or the default 0).
        *   `char_counts[char] = ...`: We update (or create) the entry in the `char_counts` dictionary with the new count.

3.  **Second Loop (Finding the First Unique Character):**
    *   `for i, char in enumerate(s):`:  We iterate through the string `s` *again*, but this time we also keep track of the *index* of each character using `enumerate`.
    *   `if char_counts[char] == 1:`: Inside the loop, we check the count of the current character `char` in our `char_counts` dictionary.  If the count is equal to 1, it means that this character appears only once in the string.
    *   `return i`: If we find a character with a count of 1, we immediately return its index `i`.  This is because we want to find the *first* such character.

4.  **`return -1`:**  If the loop completes without finding any character with a count of 1, it means that there are no non-repeating characters in the string. In this case, we return -1 as specified in the problem.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string.  We iterate through the string twice (once to count and once to find the unique character), but these are linear operations.
*   **Space Complexity:** O(1) in the best case(all letters are the same) and O(n) in the worst case where all letters are different.  In reality, since we are working with characters, the size of `char_counts` is limited by the number of unique characters in the character set (e.g., ASCII or Unicode). So it is technically O(1), as the space used by the hashtable won't grow beyond a certain limit. However, it is important to understand the worst case scenario.
