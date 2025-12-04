Okay, here's a random DSA problem and a Python solution:

**Problem:  First Unique Character in a String**

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

    # Use a dictionary to store character counts.
    char_counts = {}

    # Count the occurrences of each character.
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1  #Use get to handle missing keys

    # Iterate through the string again to find the first character with count 1.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1

# Example usage
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"'{string1}': {first_unique_char(string1)}")
print(f"'{string2}': {first_unique_char(string2)}")
print(f"'{string3}': {first_unique_char(string3)}")
```

**Explanation:**

1.  **Character Counting:**
    *   We use a dictionary `char_counts` to store the frequency of each character in the input string `s`.
    *   We iterate through the string, and for each character, we increment its count in the `char_counts` dictionary. The `char_counts.get(char, 0) + 1` pattern is used to handle cases where a character is encountered for the first time. `get(char, 0)` returns 0 if `char` is not a key in the dictionary, avoiding a `KeyError`.

2.  **Finding the First Unique Character:**
    *   We iterate through the string `s` again, this time along with its index `i` using `enumerate`.
    *   For each character `char` at index `i`, we check if its count in `char_counts` is equal to 1.
    *   If the count is 1, it means the character is unique, and we immediately return its index `i`.

3.  **No Unique Character:**
    *   If the loop completes without finding any unique character (i.e., all characters have counts greater than 1), we return -1 to indicate that no unique character exists in the string.

**Time Complexity:** O(n), where n is the length of the string. We iterate through the string twice.
**Space Complexity:** O(1). In the worst-case scenario, the `char_counts` dictionary will store all unique characters in the string.  Since the number of unique characters is limited by the size of the alphabet (e.g., 26 for lowercase English letters), the space complexity is considered constant.

This solution is relatively straightforward and efficient for finding the first unique character in a string.
