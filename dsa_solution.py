Okay, here's a randomly generated DSA problem and a Python solution:

**Problem: Word Ladder Length**

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:

1.  Only one letter can be changed at a time.
2.  Each transformed word must exist in the `wordList`.

Return 0 if no such transformation sequence exists.

**Example:**

```
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
```

**Python Solution (using Breadth-First Search - BFS):**

```python
from collections import deque

def wordLadderLength(beginWord, endWord, wordList):
    """
    Finds the length of the shortest word ladder from beginWord to endWord.

    Args:
        beginWord: The starting word.
        endWord: The target word.
        wordList: The list of valid words.

    Returns:
        The length of the shortest word ladder, or 0 if none exists.
    """

    if endWord not in wordList:
        return 0

    wordSet = set(wordList)  # Convert to set for faster lookup
    queue = deque([(beginWord, 1)])  # (word, level)
    visited = {beginWord}

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):
            for char_code in range(ord('a'), ord('z') + 1):
                new_char = chr(char_code)
                new_word = word[:i] + new_char + word[i+1:]

                if new_word in wordSet and new_word not in visited:
                    queue.append((new_word, level + 1))
                    visited.add(new_word)

    return 0  # No path found


# Example Usage:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

result = wordLadderLength(beginWord, endWord, wordList)
print(f"Shortest word ladder length: {result}")  # Output: 5


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

result = wordLadderLength(beginWord, endWord, wordList)
print(f"Shortest word ladder length: {result}") #Output: 0
```

**Explanation:**

1.  **Initialization:**
    *   We first check if the `endWord` is present in the `wordList`. If not, there's no possible ladder, so we return 0.
    *   We convert the `wordList` into a `wordSet` (using `set()`) for faster lookup (checking if a word exists).
    *   We use a `deque` (from the `collections` module) to implement a queue for BFS.  Each element in the queue is a tuple: `(word, level)`, where `word` is the current word, and `level` is the length of the path to reach that word from the `beginWord`. The initial queue contains `(beginWord, 1)`.
    *   We also keep a `visited` set to avoid cycles and redundant explorations. We add the `beginWord` to the `visited` set initially.

2.  **Breadth-First Search (BFS):**
    *   The `while queue:` loop continues as long as there are words to explore in the queue.
    *   Inside the loop:
        *   We `popleft()` to get the next word and its level from the queue.
        *   If the `word` is equal to the `endWord`, we've found the shortest path, and we return the `level`.
        *   **Generating Neighboring Words:**  For each letter in the current word (using `for i in range(len(word)):`), we iterate through all possible characters 'a' to 'z' (using `for char_code in range(ord('a'), ord('z') + 1):`).  We construct a `new_word` by replacing the character at position `i` with the current character.  This effectively generates all possible one-letter-different words.
        *   **Checking Validity and Visiting:** We check two things:
            *   `new_word in wordSet`:  Is the `new_word` present in the valid `wordList`?
            *   `new_word not in visited`: Have we already visited this word?  We want to explore it only once.
            *   If both conditions are true, we add the `new_word` to the queue with an incremented `level` (`level + 1`), and we mark it as `visited`.

3.  **No Path Found:**
    *   If the loop completes without finding the `endWord`, it means there's no valid word ladder. In this case, we return 0.

**Key improvements in this solution:**

*   **Using a Set:** Converting `wordList` to a `set` significantly speeds up the `in` operation when checking if a neighboring word is valid.
*   **BFS:** Breadth-First Search guarantees finding the *shortest* path (in terms of the number of transformations) if a path exists.
*   **Visited Set:** Prevents cycles and redundant processing, making the algorithm more efficient.
*   **Clear Code:**  The code is structured with comments to explain each step.

This problem and solution demonstrate a common DSA pattern: using BFS to find the shortest path in a graph-like structure where the nodes are words, and edges connect words that differ by one letter.
