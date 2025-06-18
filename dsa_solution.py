Okay, here's a random DSA problem, along with a Python solution and explanation.

**Problem:  First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

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
def first_unique_char(s):
  """
  Finds the index of the first unique character in a string.

  Args:
    s: The input string.

  Returns:
    The index of the first unique character, or -1 if none exists.
  """

  char_counts = {}  # Dictionary to store character counts

  # Count the occurrences of each character
  for char in s:
    char_counts[char] = char_counts.get(char, 0) + 1

  # Iterate through the string and check for the first character with a count of 1
  for i in range(len(s)):
    if char_counts[s[i]] == 1:
      return i

  return -1  # No unique character found


# Example Usage
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode"))  # Output: 2
print(first_unique_char("aabb"))  # Output: -1
```

**Explanation:**

1. **`char_counts = {}`:**  We initialize an empty dictionary called `char_counts`. This dictionary will store each character in the string `s` as a key, and the number of times that character appears as the value.

2. **`for char in s:`:** We iterate through each character in the input string `s`.

3. **`char_counts[char] = char_counts.get(char, 0) + 1`:** For each character, we update its count in the `char_counts` dictionary. `char_counts.get(char, 0)` tries to retrieve the current count of `char`. If `char` is not yet in the dictionary, it returns 0 (the default value).  We then add 1 to this value and assign it back to `char_counts[char]`. This efficiently counts the occurrences of each character.

4. **`for i in range(len(s)):`:**  After counting the occurrences of all characters, we iterate through the string `s` again, this time using indices.

5. **`if char_counts[s[i]] == 1:`:**  For each character at index `i`, we check its count in the `char_counts` dictionary. If the count is equal to 1, it means that the character appears only once in the string.

6. **`return i`:** If we find a character with a count of 1, we immediately return its index `i`.  This is the first unique character in the string.

7. **`return -1`:** If the loop completes without finding any unique characters (i.e., no character has a count of 1), we return -1 to indicate that there are no unique characters in the string.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string `s`.  We iterate through the string twice, once to count the characters and once to find the first unique character.

*   **Space Complexity:** O(1).  Although we use a dictionary, the size of the dictionary is limited by the number of unique characters in the string.  In the worst case (all characters are unique), the space complexity would be O(26) = O(1) since it will be bounded by the number of letters in the English alphabet. In general, if the string could use unicode chars, then this space complexity would be O(k), where k is the number of unique characters.
