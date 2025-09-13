Okay, here's a random DSA problem and a Python solution:

**Problem:  First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

**Example:**

*   `s = "leetcode"`  Output: `0` (because 'l' is the first unique character and it's at index 0)
*   `s = "loveleetcode"` Output: `2` (because 'v' is the first unique character and it's at index 2)
*   `s = "aabb"` Output: `-1` (because there are no unique characters)

**Solution (Python):**

```python
def firstUniqChar(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    # Use a dictionary to store character counts.
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1  # Increment count, default to 0 if not present

    # Iterate through the string again to find the first character with a count of 1.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1


# Example Usage
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"'{string1}': {firstUniqChar(string1)}")
print(f"'{string2}': {firstUniqChar(string2)}")
print(f"'{string3}': {firstUniqChar(string3)}")
```

**Explanation:**

1.  **Character Counting:**
    *   A dictionary `char_counts` is used to store the frequency of each character in the string.
    *   The code iterates through the string `s`. For each character:
        *   `char_counts.get(char, 0) + 1`: This cleverly retrieves the current count of the character `char` from the dictionary. If the character is not yet in the dictionary, `get(char, 0)` returns 0 (the default value).  Then, it increments the count by 1.

2.  **Finding the First Unique Character:**
    *   The code iterates through the string `s` *again*, this time keeping track of the index `i` using `enumerate`.
    *   For each character `char` at index `i`, it checks if `char_counts[char]` is equal to 1.  If it is, that means the character appeared only once in the string.  The function immediately returns the index `i`.

3.  **No Unique Character:**
    *   If the loop completes without finding any character with a count of 1, it means there are no unique characters in the string.  In this case, the function returns `-1`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  We iterate through the string twice.
*   **Space Complexity:** O(1).  While we use a dictionary, in the worst case, it will store all distinct characters of the string. In the worst case scenario all 26 lowercase English alphabet will be stored. Therefore we can consider it as O(1).
