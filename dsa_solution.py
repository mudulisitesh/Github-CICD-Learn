Okay, here's a DSA problem and a Python solution with explanations:

**Problem:**

**Group Anagrams**

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Python Solution:**

```python
from collections import defaultdict

def groupAnagrams(strs):
    """
    Groups anagrams in a list of strings.

    Args:
    strs: A list of strings.

    Returns:
    A list of lists, where each inner list contains anagrams.
    """

    anagram_groups = defaultdict(list)  # Dictionary to store anagrams, key is the sorted string

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to use as the key
        anagram_groups[sorted_s].append(s)  # Add the original string to the corresponding group

    return list(anagram_groups.values())  # Return the values (lists of anagrams)
# Example usage:
strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print(result) # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Explanation:**

1.  **`defaultdict(list)`:**  We use `defaultdict(list)` from the `collections` module.  A `defaultdict` is like a regular dictionary, but if you try to access a key that doesn't exist, it automatically creates that key with a default value (in this case, an empty list).  This is perfect for our use case, as we don't need to check if a sorted string (the key) exists before appending to its anagram list.

2.  **Iteration:** The code iterates through each string `s` in the input list `strs`.

3.  **Sorting:** Inside the loop, `sorted(s)` sorts the characters of the string `s` alphabetically.  The `"".join()` then converts the sorted list of characters back into a string. This sorted string becomes the unique key for all anagrams of `s`.

4.  **Grouping:**  `anagram_groups[sorted_s].append(s)` appends the *original* string `s` to the list associated with the `sorted_s` key in the `anagram_groups` dictionary. Because anagrams will have the same sorted string, they'll be grouped together in the same list.

5.  **Returning the Result:** Finally, `list(anagram_groups.values())` retrieves all the values from the `anagram_groups` dictionary (which are the lists of anagrams) and converts them into a list of lists, which is the desired output format.

**Time and Space Complexity:**

*   **Time Complexity:** O(N * K * log K), where N is the number of strings in the input list `strs`, and K is the maximum length of a string in `strs`.  The K * log K part comes from sorting each string.

*   **Space Complexity:** O(N * K) in the worst case, where N is the number of strings and K is the maximum length of a string. This is because, in the worst case (e.g., all strings are unique), the `anagram_groups` dictionary will store all N strings. Each string can have length at most K.
