Okay, here's a random DSA problem and a Python solution.

**Problem:**

**First Unique Character in a String**

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Example:**

*   **Input:** `s = "leetcode"`
*   **Output:** `0`

*   **Input:** `s = "loveleetcode"`
*   **Output:** `2`

*   **Input:** `s = "aabb"`
*   **Output:** `-1`

**Explanation:**

The problem requires analyzing a string to find the first character that appears only once.  A frequency counter approach is efficient for this.

**Python Code Solution:**

```python
def firstUniqChar(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """

    # 1. Frequency Counter (using dictionary)
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # 2. Iterate through the string to find the first character with count 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    # 3. If no unique character is found, return -1
    return -1

# Example Usage:
print(firstUniqChar("leetcode"))  # Output: 0
print(firstUniqChar("loveleetcode")) # Output: 2
print(firstUniqChar("aabb")) # Output: -1
```

**Explanation of the Code:**

1.  **Frequency Counter:**
    *   A dictionary `char_counts` is used to store the frequency of each character in the string `s`.
    *   The code iterates through the string, and for each character:
        *   It checks if the character is already in the `char_counts` dictionary.
        *   If the character is present, its count is incremented.
        *   If the character is not present, it is added to the dictionary with a count of 1.  `char_counts.get(char, 0)` is a convenient way to handle both cases.

2.  **Find First Unique Character:**
    *   The code then iterates through the string `s` again, this time using `enumerate` to get both the index `i` and the character `char` at each position.
    *   For each character, it checks its count in the `char_counts` dictionary.
    *   If the count of the character is 1 (meaning it is a non-repeating character), the function immediately returns the index `i`.

3.  **No Unique Character:**
    *   If the loop completes without finding any character with a count of 1, it means there are no unique characters in the string. In this case, the function returns -1.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the string.  We iterate through the string twice, but the overall complexity is still linear.
*   **Space Complexity:** O(1), or more precisely O(k), where k is the number of unique characters in the string (at most 26 for lowercase English alphabet). In practice, this is often treated as constant space because the alphabet size is relatively small and fixed.

**Why this is a good solution:**

*   **Clear and Readable:**  The code is well-structured and easy to understand.  The comments explain each step.
*   **Efficient:** It uses a hash table (dictionary) to count character frequencies, which provides fast lookups (O(1) on average).
*   **Concise:**  The solution is relatively short and avoids unnecessary complexity.
*   **Handles edge cases:**  It correctly handles cases where there are no unique characters.
