Okay, here's a DSA problem and its Python solution. I've tried to pick one that isn't *too* common but still illustrates some useful concepts.

**Problem:  Friend Circle Queries**

Imagine you're building a social network.  You start with a collection of users who are initially not connected (each in their own "friend circle").  You receive a series of connection requests: "Make user A a friend of user B."  Your task is to determine, after each connection request, the *size* of the largest friend circle in the network.

**Input:**

A list of tuples, where each tuple represents a connection request. Each tuple contains two integers, representing the user IDs to connect (e.g., `(1, 2)` means connect user 1 and user 2). User IDs are 1-indexed and are assumed to be positive integers.

**Output:**

A list of integers, where the i-th integer in the list represents the size of the largest friend circle *after* processing the i-th connection request.

**Example:**

```
Input:
connections = [(1, 2), (1, 3), (4, 5), (2, 6), (5, 7)]

Output:
[2, 3, 2, 4, 4]
```

**Explanation of the Example:**

1.  `(1, 2)`: Users 1 and 2 become friends. The largest circle is of size 2 (users 1, 2).
2.  `(1, 3)`: User 3 becomes friends with the circle containing 1 and 2.  The largest circle is of size 3 (users 1, 2, 3).
3.  `(4, 5)`: Users 4 and 5 become friends. The largest circle is of size 3 (users 1, 2, 3).  There's also a circle of size 2 (users 4, 5).
4.  `(2, 6)`: User 6 becomes friends with the circle containing 1, 2, and 3. The largest circle is of size 4 (users 1, 2, 3, 6).
5.  `(5, 7)`: User 7 becomes friends with the circle containing 4 and 5. The largest circle is of size 4 (users 1, 2, 3, 6).  There's now a circle of size 3 (users 4, 5, 7).

**Python Solution (Using Disjoint Set Union / Union-Find):**

```python
class DisjointSet:
    def __init__(self):
        self.parent = {}  # Maps user to its parent
        self.size = {}    # Maps user to the size of its circle
        self.max_size = 0

    def find(self, user):
        """Finds the representative (root) of the set containing the user."""
        if user not in self.parent:
            self.parent[user] = user
            self.size[user] = 1
            self.max_size = max(self.max_size, 1) # Update initial max_size
            return user

        if self.parent[user] != user:
            self.parent[user] = self.find(self.parent[user])  # Path compression
        return self.parent[user]

    def union(self, user1, user2):
        """Merges the sets containing user1 and user2."""
        root1 = self.find(user1)
        root2 = self.find(user2)

        if root1 != root2:
            # Union by size (smaller tree attaches to larger)
            if self.size[root1] < self.size[root2]:
                root1, root2 = root2, root1  # Ensure root1 is the larger set

            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            del self.size[root2]  # Remove the size entry from the old root

            self.max_size = max(self.max_size, self.size[root1])
            return True  # Indicate a union happened
        return False  # Indicate no union happened (already in the same set)


def friend_circle_queries(connections):
    """
    Processes connection requests and returns the size of the largest friend circle
    after each request.
    """
    dsu = DisjointSet()
    results = []
    for u, v in connections:
        dsu.union(u, v)  # Union the two users
        results.append(dsu.max_size)  # Add the current max circle size to results
    return results


# Example Usage:
connections = [(1, 2), (1, 3), (4, 5), (2, 6), (5, 7)]
output = friend_circle_queries(connections)
print(output)  # Output: [2, 3, 2, 4, 4]


connections2 = [(100, 1), (1, 2), (100, 3), (1, 4), (2, 5), (3, 6), (1, 7), (8, 9), (10, 11), (10, 12), (10, 13), (8, 14), (15, 16), (17, 18), (15, 19), (17, 20), (15, 21), (17, 22), (15, 23), (17, 24), (15, 25), (1, 26), (17, 27), (1, 28), (17, 29)]
output2 = friend_circle_queries(connections2)
print(output2)
```

**Key Concepts and Explanation:**

1.  **Disjoint Set Union (DSU) / Union-Find:** This data structure is perfect for problems that involve tracking connected components (sets) and efficiently merging them.

2.  **`DisjointSet` Class:**
    *   `parent`: A dictionary that maps each user to its "parent" in the disjoint set forest. Initially, each user is its own parent (representing a separate set).
    *   `size`: A dictionary that maps each root user (representative) to the size of its set.
    *   `max_size`:  An attribute to keep track of the maximum size of any friend circle.  This allows us to retrieve the max size in O(1) time.

3.  **`find(user)` Method:**
    *   **Path Compression:** This is a crucial optimization. When finding the representative of a user, it updates the user's parent to point directly to the representative. This flattens the tree structure, making future `find` operations faster.
    *   If a user is not in the dictionary yet, it initializes the user with itself as parent and a size of 1.

4.  **`union(user1, user2)` Method:**
    *   Finds the representatives (`root1`, `root2`) of the sets containing `user1` and `user2`.
    *   If the representatives are different (meaning the users are in different sets), it merges the sets.
    *   **Union by Size (or Rank):**  This is another optimization. It attaches the smaller tree (set) to the root of the larger tree (set). This helps to keep the trees relatively balanced, preventing worst-case scenarios where `find` operations could take linear time. `find` becomes almost O(1) on average with both path compression and union by size.  We are using Union by size here.

5.  **`friend_circle_queries(connections)` Function:**
    *   Iterates through the `connections` list.
    *   For each connection `(u, v)`, it calls `dsu.union(u, v)` to merge the sets containing `u` and `v`.
    *   Appends `dsu.max_size` (the current maximum circle size) to the `results` list.

**Time Complexity:**

*   With path compression and union by size, the `find` and `union` operations take almost constant time on average (amortized O(α(n)), where α(n) is the inverse Ackermann function, which grows extremely slowly and can be considered practically constant).
*   Therefore, the overall time complexity of `friend_circle_queries` is O(m * α(n)), where 'm' is the number of connection requests and 'n' is the number of users, effectively O(m).

**Space Complexity:**

*   O(n), where n is the number of users, due to the `parent` and `size` dictionaries in the `DisjointSet` class.
*   O(m) to store the `results`.
