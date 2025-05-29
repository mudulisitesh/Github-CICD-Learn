Okay, here's a problem focusing on array manipulation and hash maps, along with a Python solution:

**Problem:  Find the First Repeating Element**

Given an array of integers, find the first repeating element in the array. In other words, find the element that occurs more than once and whose first occurrence has the smallest index.  If no element repeats, return -1.

**Example:**

```
Input:  arr = [10, 5, 3, 4, 3, 5, 6]
Output: 5 (because 5 is the first element that repeats, and its first occurrence appears before the first occurrence of 3)

Input: arr = [6, 10, 5, 4, 9]
Output: -1 (no repeating element)
```

**Explanation:**

The core idea is to iterate through the array and keep track of the elements we've seen so far. A hash map (dictionary in Python) is ideal for this. We want to find the element that appears *again* first.

**Python Code Solution:**

```python
def find_first_repeating(arr):
  """
  Finds the first repeating element in an array.

  Args:
    arr: A list of integers.

  Returns:
    The first repeating element in the array. If no element repeats, returns -1.
  """
  seen = {}  # Dictionary to store elements and their first index
  min_index = float('inf')  # Initialize with a large value
  repeating_element = -1

  for i, num in enumerate(arr):
    if num in seen:
      # This element has been seen before
      if seen[num] < min_index:  # Check if its first index is smaller than the current min_index
          min_index = seen[num]
          repeating_element = num
    else:
      seen[num] = i  # Store the index of the first occurrence

  if repeating_element == -1:
    return -1
  else:
    return repeating_element

# Example usage:
arr1 = [10, 5, 3, 4, 3, 5, 6]
print(f"Input: {arr1}, Output: {find_first_repeating(arr1)}")  # Output: 5

arr2 = [6, 10, 5, 4, 9]
print(f"Input: {arr2}, Output: {find_first_repeating(arr2)}")  # Output: -1

arr3 = [1, 2, 3, 4, 5, 6, 1]
print(f"Input: {arr3}, Output: {find_first_repeating(arr3)}") # Output: 1

arr4 = [1, 2, 3, 4, 5, 6]
print(f"Input: {arr4}, Output: {find_first_repeating(arr4)}") # Output: -1

arr5 = [1, 1, 2, 2, 3, 3]
print(f"Input: {arr5}, Output: {find_first_repeating(arr5)}") # Output: 1
```

**Explanation of the Code:**

1. **`seen = {}`:**  We create an empty dictionary `seen` to store each element encountered in the array along with its index.

2. **`min_index = float('inf')`:** We initialize `min_index` to positive infinity.  This variable will store the smallest index of the first occurrence of a repeating element.

3. **`repeating_element = -1`:**  We initialize `repeating_element` to -1, which will be the return value if no element repeats.

4. **`for i, num in enumerate(arr):`:**  We iterate through the array using `enumerate` to get both the index (`i`) and the value (`num`) of each element.

5. **`if num in seen:`:**
   - If `num` is already in the `seen` dictionary, it means we've encountered this element before, so it's a repeating element.
   - `if seen[num] < min_index:`:  This is a crucial check.  We need to make sure the *first* occurrence of this repeating element is earlier than any other repeating element we've seen so far.  `seen[num]` gives us the index of the first occurrence.
   - `min_index = seen[num]` and `repeating_element = num`: If the first occurrence is earlier, we update `min_index` and `repeating_element`.

6. **`else:`:**
   - If `num` is not in the `seen` dictionary, it means this is the first time we're seeing this element.
   - `seen[num] = i`: We add the element `num` to the `seen` dictionary along with its index `i`.

7. **`return repeating_element`:**  After iterating through the entire array, we return `repeating_element`. If no element repeated, it will still be -1.

**Time and Space Complexity:**

- **Time Complexity: O(n)** -  We iterate through the array once.  Dictionary lookups ( `if num in seen:` and `seen[num]`) take approximately constant time on average (O(1)).
- **Space Complexity: O(n)** - In the worst case, if all the elements in the array are unique, the `seen` dictionary will store all `n` elements.

**Why this is a good DSA problem:**

*   **Array Traversal:** It involves iterating through an array.
*   **Hash Maps/Dictionaries:**  It effectively utilizes hash maps for efficient tracking of elements.
*   **Edge Cases:** It requires handling the case where no element repeats.
*   **Optimization:**  It encourages thinking about finding the *first* repeating element, not just any repeating element.  The `min_index` variable is key to that.
*   **Common Pattern:** The "using a dictionary to track elements seen" pattern is very common in many algorithm problems.
