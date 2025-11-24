Okay, here's a randomly generated DSA problem, followed by a Python solution with explanations:

**Problem: First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example 1:**

Input: `s = "leetcode"`
Output: 0

**Example 2:**

Input: `s = "loveleetcode"`
Output: 2

**Example 3:**

Input: `s = "aabb"`
Output: -1

**Python Solution:**

```python
def first_uniq_char(s):
    """
    Finds the index of the first unique character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first unique character, or -1 if none exists.
    """

    # Create a dictionary to store the frequency of each character.
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string and check if the character's count is 1.
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # If no unique character is found, return -1.
    return -1

# Example usage:
string1 = "leetcode"
print(f"First unique char in '{string1}': {first_uniq_char(string1)}")  # Output: 0

string2 = "loveleetcode"
print(f"First unique char in '{string2}': {first_uniq_char(string2)}")  # Output: 2

string3 = "aabb"
print(f"First unique char in '{string3}': {first_uniq_char(string3)}")  # Output: -1

string4 = "dddccdbba"
print(f"First unique char in '{string4}': {first_uniq_char(string4)}") # Output: 8

string5 = "z"
print(f"First unique char in '{string5}': {first_uniq_char(string5)}") #Output: 0
```

**Explanation:**

1. **`first_uniq_char(s)` Function:**
   - Takes the input string `s` as an argument.

2. **Character Frequency Counting:**
   - `char_counts = {}`:  Initializes an empty dictionary called `char_counts` to store the frequency of each character.
   - `for char in s:`:  Iterates through each character in the input string.
   - `char_counts[char] = char_counts.get(char, 0) + 1`:
     - `char_counts.get(char, 0)`:  This tries to retrieve the current count of the character `char` from the `char_counts` dictionary.  If the character is not already in the dictionary, `get()` returns 0 (the default value).
     - `+ 1`:  Increments the count by 1.
     - `char_counts[char] = ...`:  Updates the count for the character in the dictionary. This effectively counts the occurrences of each character in the string.

3. **Finding the First Unique Character:**
   - `for i, char in enumerate(s):`:  Iterates through the string again, this time using `enumerate()` to get both the index (`i`) and the character (`char`) at each position.
   - `if char_counts[char] == 1:`:  Checks if the count of the current character in the `char_counts` dictionary is equal to 1.  If it is, it means the character appears only once in the string.
   - `return i`:  If the character is unique, the function immediately returns its index (`i`).

4. **No Unique Character Found:**
   - `return -1`:  If the loop completes without finding any unique characters, it means all characters in the string appear more than once.  In this case, the function returns -1.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the string `s`. The code iterates through the string twice in the worst case. The dictionary operations (get and set) have an average time complexity of O(1).
- **Space Complexity:** O(1).  The `char_counts` dictionary stores the frequency of each character. In the worst case, all characters in the string are unique, and the dictionary will store all the characters.  Since the number of possible characters is limited (e.g., 26 for lowercase English letters or 128 for ASCII), the space used by the dictionary is considered constant. However, in a more general Unicode case, the space complexity could approach O(n) in a highly unusual case where *every* character in a large string is unique.

**Why this solution is good:**

*   **Clear and Readable:** The code is straightforward and easy to understand.
*   **Efficient:** The use of a dictionary allows for efficient character counting and lookups.
*   **Correct:** The solution handles the edge cases (empty string, no unique characters) correctly.
*   **Well-Documented:** The code includes comments explaining the purpose of each section.
