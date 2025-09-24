Okay, here's a DSA problem with a Python solution:

**Problem:**

**Group Anagrams**

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

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

*   `1 <= strs.length <= 10^4`
*   `0 <= strs[i].length <= 100`
*   `strs[i]` consists of lowercase English letters.

**Python Solution:**

```python
from collections import defaultdict

def groupAnagrams(strs):
    """
    Groups anagrams from a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = defaultdict(list)  # Use defaultdict for convenient grouping

    for s in strs:
        # Create a sorted string as a key (anagram signature)
        sorted_s = "".join(sorted(s))

        # Add the original string to the corresponding group
        anagram_groups[sorted_s].append(s)

    # Return the values (list of anagrams) of the dictionary
    return list(anagram_groups.values())


# Example Usage
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs1))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (order may vary)

strs2 = [""]
print(groupAnagrams(strs2)) #Output: [['']]

strs3 = ["a"]
print(groupAnagrams(strs3)) # Output: [['a']]
```

**Explanation:**

1.  **`defaultdict(list)`:**  We use `defaultdict(list)` from the `collections` module. This creates a dictionary where, if a key is not found, it automatically creates an empty list as the default value for that key.  This is perfect for grouping.

2.  **Anagram Signature (Key):** The core idea is to create a unique identifier for each anagram group. We achieve this by sorting the characters in each string `s`.  The sorted string will be the same for all anagrams.  For example, "eat", "tea", and "ate" all become "aet" when sorted.  This "aet" becomes the key in our `anagram_groups` dictionary.

3.  **Grouping:** We iterate through the input `strs`. For each string `s`, we calculate its sorted form (`sorted_s`). We then use `anagram_groups[sorted_s].append(s)` to add the *original* string `s` to the list associated with its sorted form.

4.  **Returning the Result:** Finally, `list(anagram_groups.values())` returns a list of lists. Each inner list contains the anagrams that belong to the same group (i.e., have the same sorted form).

**Time Complexity:** O(N * K log K), where N is the number of strings in the input list, and K is the maximum length of a string.  Sorting each string takes O(K log K) time, and we do this for each of the N strings.

**Space Complexity:** O(N * K), where N is the number of strings, and K is the maximum length of a string. In the worst case, all strings are unique, and we need to store all of them in the `anagram_groups` dictionary.
