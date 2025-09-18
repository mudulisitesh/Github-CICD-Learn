Okay, here's a DSA problem and a Python solution, complete with explanations.

**Problem:**

**First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example 1:**

Input: `s = "leetcode"`
Output: `0`

**Example 2:**

Input: `s = "loveleetcode"`
Output: `2`

**Example 3:**

Input: `s = "aabb"`
Output: `-1`

**Python Solution:**

```python
def firstUniqChar(s: str) -> int:
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    char_counts = {}  # Dictionary to store character counts
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1

# Example Usage
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"First unique char in '{string1}': {firstUniqChar(string1)}")  # Output: 0
print(f"First unique char in '{string2}': {firstUniqChar(string2)}")  # Output: 2
print(f"First unique char in '{string3}': {firstUniqChar(string3)}")  # Output: -1
```

**Explanation:**

1. **Character Counting (Hash Map/Dictionary):**

   - We use a dictionary (hash map) called `char_counts` to store the frequency of each character in the string.
   - We iterate through the input string `s`. For each character:
     - `char_counts[char] = char_counts.get(char, 0) + 1` : This line efficiently updates the count.  `char_counts.get(char, 0)` retrieves the current count for the character `char`. If the character is not already in the dictionary, `get()` returns a default value of 0. We then add 1 to the count.

2. **Finding the First Unique Character:**

   - We iterate through the string `s` *again*, this time using `enumerate` to get both the index `i` and the character `char` at each position.
   - `if char_counts[char] == 1:` :  We check if the count of the current character `char` in the `char_counts` dictionary is equal to 1. If it is, it means this character appears only once in the string, so it's unique.
   - `return i`: We immediately return the index `i` of this first unique character.

3. **No Unique Character:**

   - If the loop completes without finding any character with a count of 1, it means there are no unique characters in the string. In this case, we return -1.

**Time and Space Complexity:**

- **Time Complexity:** O(N), where N is the length of the string `s`.  We iterate through the string twice (once to count characters and once to find the first unique one).
- **Space Complexity:** O(1). In the worst case, the `char_counts` dictionary might store all unique characters from the input string. However, since the input string consists of characters, and the number of possible characters is limited (e.g., ASCII characters), the space used is considered constant.  Technically for ASCII the complexity is O(256) which simplifies to O(1). If the string could contain Unicode characters, then the space complexity could potentially become O(N) in the worst case.

**Why this solution is good:**

- **Clear and Readable:**  The code is well-structured and easy to understand.
- **Efficient:**  Using a hash map (dictionary) provides fast lookups for character counts (O(1) on average).
- **Handles Edge Cases:**  It correctly returns -1 if there are no unique characters.
- **Concise:** The solution is implemented in a relatively small number of lines.