Okay, here's a DSA problem along with a Python solution:

**Problem: First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example:**

```
s = "leetcode"
Output: 0

s = "loveleetcode"
Output: 2

s = "aabb"
Output: -1
```

**Explanation:**

The problem requires you to traverse a string and identify the first character that appears only once.  A common and efficient approach is to use a hash map (dictionary in Python) to store the frequency of each character.  Then, iterate through the string again, checking the frequency of each character in the hash map. The first character with a frequency of 1 is the answer.

**Python Solution:**

```python
def first_unique_char(s: str) -> int:
    """
    Finds the index of the first unique character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    # Create a dictionary to store the frequency of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string and check for the first character with a frequency of 1
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    # If no unique character is found, return -1
    return -1


# Example Usage
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode")) # Output: 2
print(first_unique_char("aabb")) # Output: -1
```

**Explanation of the Code:**

1. **`first_unique_char(s: str) -> int:`**:  This defines the function signature, specifying that it takes a string `s` as input and returns an integer (the index or -1).

2. **`char_counts = {}`**:  Initializes an empty dictionary `char_counts`. This dictionary will store character frequencies.

3. **`for char in s:`**: This loop iterates through each character in the input string `s`.

4. **`char_counts[char] = char_counts.get(char, 0) + 1`**:  This line updates the frequency count for each character in the `char_counts` dictionary.
   - `char_counts.get(char, 0)`: This attempts to retrieve the current count for the character `char` from the dictionary. If the character is not already in the dictionary, it returns a default value of 0.
   - `+ 1`:  Increments the count by 1.

5. **`for i in range(len(s)):`**: This loop iterates through the string `s` again, but this time using the index `i`.

6. **`if char_counts[s[i]] == 1:`**:  This checks if the character at index `i` has a frequency of 1 in the `char_counts` dictionary.

7. **`return i`**: If the character has a frequency of 1, it means it's a unique character. The function immediately returns the index `i`.

8. **`return -1`**: If the loop completes without finding any character with a frequency of 1, it means there are no unique characters in the string. In this case, the function returns -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  The code iterates through the string twice in the worst case.
*   **Space Complexity:** O(1). The space complexity is constant because the `char_counts` dictionary can store at most 26 unique characters (assuming the input string contains only lowercase English letters).  In general, it depends on the size of the alphabet. If we're dealing with Unicode, it could be larger, but it's still bounded.  Therefore, we can consider the space complexity O(1) or O(k), where k is the size of the character set.
