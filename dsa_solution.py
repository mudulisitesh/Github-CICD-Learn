Okay, here's a DSA problem and a Python solution:

**Problem: Implement LRU (Least Recently Used) Cache**

Design and implement a data structure for a Least Recently Used (LRU) cache. It should support the following operations:

*   **`get(key)`**: Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
*   **`put(key, value)`**: Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a **positive** capacity.

**Constraints:**

*   `1 <= capacity <= 3000`
*   `0 <= key <= 10000`
*   `0 <= value <= 10^5`
*   At most `2 * 10^5` calls will be made to `get` and `put`.

**Example:**

```python
cache = LRUCache(2) # capacity is 2

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4
```

**Python Solution:**

```python
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key: Node
        self.left = Node(0, 0) # Dummy head node
        self.right = Node(0, 0) # Dummy tail node
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node):
        """Removes a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node: Node):
        """Inserts a node right before the tail."""
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = node
        next_node.prev = node
        node.next = next_node
        node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node) # Remove from its current position
            self._insert(node) # Move to the most recently used
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            del self.cache[key] # Remove from cache.  Important for updating
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            # Evict the least recently used (left.next)
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

# Example Usage:
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)    # evicts key 2
print(cache.get(2))       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4
```

**Explanation:**

1.  **`Node` Class:** Represents a node in the doubly linked list, storing the key, value, `next` pointer, and `prev` pointer.

2.  **`LRUCache` Class:**
    *   **`__init__(self, capacity: int)`:** Initializes the cache with the given capacity.
        *   `self.capacity`: Stores the maximum capacity of the cache.
        *   `self.cache`: A dictionary (hash map) that stores key-value pairs, where the value is a `Node` object.  This allows O(1) access for get and put operations.
        *   `self.left` and `self.right`: Dummy nodes that mark the beginning and end of the doubly linked list. These make insertion and removal operations cleaner and avoid edge case checks.

    *   **`_remove(self, node: Node)`:**  Removes a given `node` from the doubly linked list.  It updates the `next` and `prev` pointers of the surrounding nodes.

    *   **`_insert(self, node: Node)`:** Inserts a given `node` into the doubly linked list *right before* the `self.right` (tail) node.  This makes the newly inserted node the most recently used.

    *   **`get(self, key: int) -> int`:**
        *   Checks if the `key` exists in `self.cache`.
        *   If the `key` exists:
            *   Retrieves the corresponding `Node` from the `self.cache`.
            *   Removes the `node` from its current position in the linked list using `self._remove(node)`.
            *   Inserts the `node` at the tail (most recently used position) using `self._insert(node)`.
            *   Returns the `node.val` (the value associated with the key).
        *   If the `key` doesn't exist, returns `-1`.

    *   **`put(self, key: int, value: int) -> None`:**
        *   If the `key` already exists in `self.cache`:
            *   Remove the existing node using `self._remove()`.
            *   Remove the item from the `self.cache`.  This is critical to ensure we update the node. If we don't, we will insert a *duplicate* entry in the DLL, and the cache length will grow larger than its capacity.
        *   Creates a new `Node` with the given `key` and `value`.
        *   Adds the `key`-`node` pair to the `self.cache`.
        *   Inserts the `node` at the tail (most recently used position) using `self._insert(node)`.
        *   Checks if the current size of `self.cache` exceeds `self.capacity`.
        *   If the cache is full:
            *   Removes the least recently used node (the one immediately after `self.left`, which is the dummy head) using `self._remove(self.left.next)`.
            *   Removes the corresponding entry from `self.cache` using `del self.cache[lru.key]` (where `lru` is the least recently used node).  Again, deletion from the cache is critical.

**Time Complexity:**

*   `get()`: O(1) (due to the hash map `self.cache` and doubly linked list operations)
*   `put()`: O(1) (due to the hash map `self.cache` and doubly linked list operations)

**Space Complexity:**

*   O(capacity) - The cache stores up to `capacity` key-value pairs, and each key-value pair takes up constant space.  The linked list itself contributes a space complexity proportional to the capacity.
