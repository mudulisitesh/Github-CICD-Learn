Okay, here's a randomly generated DSA problem and a Python solution:

**Problem:**

**Longest Substring Without Repeating Characters**

Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Constraints:**

*   `0 <= s.length <= 5 * 104`
*   `s` consists of English letters, digits, symbols and spaces.

**Python Solution:**

```python
def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """

    n = len(s)
    if n == 0:
        return 0

    char_index_map = {}  # Stores the most recent index of each character
    start = 0          # Start index of the current substring
    max_len = 0        # Maximum length found so far

    for end in range(n):
        char = s[end]

        if char in char_index_map and char_index_map[char] >= start:
            # If the character is already in the current substring, move the start index
            start = char_index_map[char] + 1

        char_index_map[char] = end  # Update the index of the current character
        max_len = max(max_len, end - start + 1)  # Update the maximum length

    return max_len
```

**Explanation:**

1.  **Initialization:**
    *   `n = len(s)`: Get the length of the input string.
    *   `char_index_map = {}`:  A dictionary to store the most recent index of each character encountered.  This acts as our "window" to check for repeating characters.
    *   `start = 0`:  Index representing the beginning of the current substring being considered.
    *   `max_len = 0`:  Variable to track the length of the longest substring found so far.

2.  **Sliding Window:**
    *   The `for end in range(n)` loop iterates through the string, with `end` representing the ending index of the current substring.
    *   `char = s[end]`: Get the character at the current ending index.

3.  **Checking for Repeating Characters:**
    *   `if char in char_index_map and char_index_map[char] >= start:`: This is the core logic.  It checks:
        *   `char in char_index_map`:  If the current character `char` is already present in the `char_index_map`.  If it's not, it means we haven't seen it in the current substring.
        *   `char_index_map[char] >= start`:  More importantly, it checks if the *last seen* index of `char` is within the current substring (i.e., greater than or equal to the `start` index).  If it is, it means we have a repeating character within our current substring.
    *   If a repeating character is found within the current substring, the `start` index is updated to `char_index_map[char] + 1`.  This effectively "slides" the window to start after the previous occurrence of the repeating character.

4.  **Updating Character Index and Maximum Length:**
    *   `char_index_map[char] = end`: Update the most recent index of the current character in the `char_index_map`.
    *   `max_len = max(max_len, end - start + 1)`: Update `max_len` with the length of the current substring (`end - start + 1`) if it's longer than the current maximum.

5.  **Return:**
    *   `return max_len`: Finally, the function returns the `max_len`, which represents the length of the longest substring without repeating characters.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string.  The `for` loop iterates through the string once, and the dictionary operations (lookup and insertion) take approximately O(1) time on average.
*   **Space Complexity:** O(min(m, n)), where n is the length of the string, and m is the size of the character set.  In the worst case, the `char_index_map` can store the indices of all unique characters in the string.  However, if the character set is smaller than the string length, the space used will be limited by the size of the character set.  For example, if the string consists only of lowercase English letters, the space complexity would be O(26) = O(1).
**How to Use:**

```python
string1 = "abcabcbb"
string2 = "bbbbb"
string3 = "pwwkew"

print(f"Longest substring of '{string1}': {length_of_longest_substring(string1)}")  # Output: 3
print(f"Longest substring of '{string2}': {length_of_longest_substring(string2)}")  # Output: 1
print(f"Longest substring of '{string3}': {length_of_longest_substring(string3)}")  # Output: 3
```
This solution uses a sliding window approach with a dictionary to efficiently track the last seen index of each character. This allows us to determine the longest substring without repeating characters in linear time.  The dictionary allows for O(1) average-case lookups.
