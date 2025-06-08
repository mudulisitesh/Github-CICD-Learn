Okay, here's a random DSA problem, along with a clear explanation and a working Python solution:

**Problem:**

**First Unique Character in a String**

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

**Explanation:**

The key idea is to count the frequency of each character in the string.  Then, we iterate through the string again, looking for the first character with a frequency of 1.

**Python Solution:**

```python
def first_unique_char(s):
    """
    Finds the index of the first unique character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    # 1. Count character frequencies
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # 2. Find the first unique character's index
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # 3. No unique character found
    return -1

# Example Usage:
string1 = "leetcode"
print(f"Input: {string1}, Output: {first_unique_char(string1)}")  # Output: 0

string2 = "loveleetcode"
print(f"Input: {string2}, Output: {first_unique_char(string2)}")  # Output: 2

string3 = "aabb"
print(f"Input: {string3}, Output: {first_unique_char(string3)}")  # Output: -1

string4 = "dddccdbba"
print(f"Input: {string4}, Output: {first_unique_char(string4)}") # Output: 8
```

**Explanation of the Code:**

1. **`first_unique_char(s)` function:**
   - Takes the input string `s` as an argument.

2. **Character Frequency Counting:**
   - `char_counts = {}`:  Initializes an empty dictionary called `char_counts` to store the frequency of each character.
   - `for char in s:`: Iterates through each character in the string `s`.
   - `char_counts[char] = char_counts.get(char, 0) + 1`:  For each character `char`:
     - `char_counts.get(char, 0)`:  Tries to get the current count of the character `char` from the `char_counts` dictionary.  If the character is not already in the dictionary, it returns 0 (the default value).
     - `+ 1`: Increments the count by 1.
     - `char_counts[char] = ...`: Updates the count of the character in the `char_counts` dictionary.

3. **Finding the First Unique Character:**
   - `for i, char in enumerate(s):`: Iterates through the string `s` again, this time using `enumerate` to get both the index (`i`) and the character (`char`).
   - `if char_counts[char] == 1:`:  Checks if the frequency of the character `char` in the `char_counts` dictionary is equal to 1.  If it is, it means the character is unique.
   - `return i`: If a unique character is found, the function immediately returns its index `i`.

4. **No Unique Character Found:**
   - `return -1`: If the loop completes without finding any unique characters (i.e., no character has a frequency of 1), the function returns `-1`.

**Time and Space Complexity:**

- **Time Complexity:** O(N), where N is the length of the string `s`.  We iterate through the string twice in the worst case.
- **Space Complexity:** O(K), where K is the number of unique characters in the string `s`.  In the worst case (if all characters are unique), K could be equal to N.  In practice, for a string using ASCII characters, K will be limited to 128 or 256, making the space complexity effectively O(1).