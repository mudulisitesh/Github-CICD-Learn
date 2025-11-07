Okay, here's a DSA problem along with a Python solution:

**Problem: Group Anagrams**

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**

```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**

```
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints:**

*   `1 <= strs.length <= 104`
*   `0 <= strs[i].length <= 100`
*   `strs[i]` consists of lowercase English letters.

**Python Solution:**

```python
def group_anagrams(strs):
    """
    Groups anagrams from a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """

    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to identify anagrams

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        else:
            anagram_groups[sorted_s] = [s]

    return list(anagram_groups.values())  # Return the values (lists of anagrams)

# Example usage
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs1))

strs2 = [""]
print(group_anagrams(strs2))

strs3 = ["a"]
print(group_anagrams(strs3))
```

**Explanation:**

1.  **`group_anagrams(strs)` function:**
    *   **`anagram_groups = {}`:** Initializes an empty dictionary.  The *keys* of this dictionary will be the *sorted versions* of the strings (e.g., "eat" becomes "aet"), and the *values* will be lists of the original strings that are anagrams of each other.
    *   **`for s in strs:`:** Iterates through each string `s` in the input list `strs`.
    *   **`sorted_s = "".join(sorted(s))`:** This is the core logic.
        *   `sorted(s)`:  Sorts the characters of the string `s` in alphabetical order.  This produces a list of characters.
        *   `"".join(...)`: Joins the sorted characters back into a single string.  This creates the "key" for our dictionary (the sorted version of the string).
    *   **`if sorted_s in anagram_groups:`:** Checks if the sorted string (`sorted_s`) is already a key in the `anagram_groups` dictionary.
        *   If it *is* a key, it means we've already found anagrams of this word.  So, we append the current string `s` to the existing list of anagrams for that key:  `anagram_groups[sorted_s].append(s)`
        *   **`else:`:** If the sorted string is *not* a key, it means this is the first time we've encountered an anagram of this type.
            *   `anagram_groups[sorted_s] = [s]`: We create a new key-value pair in the dictionary.  The key is the sorted string (`sorted_s`), and the value is a new list containing the current string `s`.
    *   **`return list(anagram_groups.values())`:** After iterating through all the strings, the `anagram_groups` dictionary contains all the anagram groups.  We extract the *values* of the dictionary (which are the lists of anagrams) and convert them to a list using `list(...)`.  This list of lists is then returned.

**How it Works (Example Breakdown):**

Let's trace the execution with the input `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

1.  **"eat"**:
    *   `sorted_s = "aet"`
    *   `anagram_groups["aet"] = ["eat"]`

2.  **"tea"**:
    *   `sorted_s = "aet"`
    *   `anagram_groups["aet"].append("tea")`  (Now `anagram_groups["aet"] = ["eat", "tea"]`)

3.  **"tan"**:
    *   `sorted_s = "ant"`
    *   `anagram_groups["ant"] = ["tan"]`

4.  **"ate"**:
    *   `sorted_s = "aet"`
    *   `anagram_groups["aet"].append("ate")` (Now `anagram_groups["aet"] = ["eat", "tea", "ate"]`)

5.  **"nat"**:
    *   `sorted_s = "ant"`
    *   `anagram_groups["ant"].append("nat")` (Now `anagram_groups["ant"] = ["tan", "nat"]`)

6.  **"bat"**:
    *   `sorted_s = "abt"`
    *   `anagram_groups["abt"] = ["bat"]`

Finally, `anagram_groups.values()` will be `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`, and the function returns this list of lists.

**Time and Space Complexity:**

*   **Time Complexity:** O(N * K log K), where N is the number of strings in the input and K is the maximum length of a string in the input.  We iterate through each string (O(N)), and for each string, we sort it (O(K log K)).
*   **Space Complexity:** O(N * K) in the worst case, where N is the number of strings and K is the maximum length of a string.  This is because, in the worst case (e.g., all strings are different and of the same length), we might store all the strings in the `anagram_groups` dictionary.

This solution is efficient and commonly used for solving the Group Anagrams problem.  It leverages the idea that anagrams have the same sorted representation.
