Okay, here's a DSA problem with a Python solution.

**Problem:**

**Find the First Non-Repeating Character in a String**

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

The problem requires you to iterate through a string and identify the first character that appears only once.

**Solution (Python):**

```python
def first_unique_char(s):
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        s: The input string.

    Returns:
        The index of the first non-repeating character, or -1 if it doesn't exist.
    """

    # Use a dictionary to store character frequencies.
    char_counts = {}

    # Count the frequency of each character.
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through the string again and find the first character with a count of 1.
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    # If no non-repeating character is found, return -1.
    return -1

# Example Usage:
string1 = "leetcode"
string2 = "loveleetcode"
string3 = "aabb"

print(f"'{string1}': {first_unique_char(string1)}")  # Output: 0
print(f"'{string2}': {first_unique_char(string2)}")  # Output: 2
print(f"'{string3}': {first_unique_char(string3)}")  # Output: -1
```

**Explanation of the Code:**

1. **Character Counting (Frequency Map):**
   - A dictionary `char_counts` is used to store the frequency of each character in the input string `s`.
   - The code iterates through the string, and for each character, it increments its count in the `char_counts` dictionary.  `char_counts.get(char, 0)` is used to efficiently handle cases where a character is encountered for the first time (if it's not in the dictionary yet, it defaults to a count of 0).

2. **Finding the First Unique Character:**
   - The code iterates through the string `s` *again*, this time using the index `i`.
   - For each character `s[i]`, it checks its count in the `char_counts` dictionary.
   - If the count of `s[i]` is equal to 1, it means that character is non-repeating.  The function immediately returns the index `i`.

3. **No Unique Character Found:**
   - If the loop completes without finding any character with a count of 1, it means there are no non-repeating characters in the string. In this case, the function returns -1.

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the string. The code iterates through the string twice.
- **Space Complexity:** O(1) in the general case.  The `char_counts` dictionary can store at most the number of unique characters in the string.  Since the input string consists of ASCII characters, the dictionary can grow to at most 256 entries, making the space complexity practically constant. In the worst-case scenario where the input alphabet is unbounded, the space complexity would be O(k), where k is the number of unique characters.

**Why this is a good DSA problem:**

- **Frequency Counting:**  It demonstrates the use of a frequency map (dictionary) for efficiently counting occurrences of elements.
- **Iteration and Lookups:** It involves iterating through a data structure (string) and performing lookups in a hash table (dictionary).
- **Edge Cases:** It includes handling the case where no unique character exists.
- **Common Pattern:**  The frequency counting pattern is very common in many string and array-based DSA problems.
