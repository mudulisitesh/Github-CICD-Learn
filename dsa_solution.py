Okay, here's a randomly generated DSA problem and a Python solution:

**Problem:**

**Find the Intersection of Multiple Sorted Arrays**

Given a list of sorted arrays, find the intersection of all the arrays. The intersection consists of the elements that are present in every single array.  Return a sorted list of the common elements.

**Example:**

```
Input:
arrays = [
  [1, 2, 2, 3, 4, 5],
  [2, 2, 3, 5],
  [2, 2, 4, 5, 6, 7]
]

Output:
[2, 5]

Explanation:
The numbers 2 and 5 are the only numbers that appear in all three arrays.  The number 2 appears multiple times, but it should only be returned once in the output.
```

**Python Solution:**

```python
def intersection_of_sorted_arrays(arrays):
    """
    Finds the intersection of multiple sorted arrays.

    Args:
        arrays: A list of sorted arrays.

    Returns:
        A sorted list containing the common elements.  Returns an empty list if there is no intersection.
    """

    if not arrays:
        return []

    if len(arrays) == 1:
        return sorted(list(set(arrays[0])))  # Handle single array case

    # Start with the first array as the potential intersection
    intersection = arrays[0]

    # Iterate through the remaining arrays and update the intersection
    for i in range(1, len(arrays)):
        intersection = find_intersection_of_two_sorted_arrays(intersection, arrays[i])

    return sorted(list(set(intersection)))  # Convert to set to remove duplicates then sort


def find_intersection_of_two_sorted_arrays(arr1, arr2):
    """
    Finds the intersection of two sorted arrays.

    Args:
        arr1: The first sorted array.
        arr2: The second sorted array.

    Returns:
        A list containing the common elements in the two arrays.
    """

    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result


# Example Usage:
arrays = [
    [1, 2, 2, 3, 4, 5],
    [2, 2, 3, 5],
    [2, 2, 4, 5, 6, 7]
]

result = intersection_of_sorted_arrays(arrays)
print(result)  # Output: [2, 5]

arrays2 = [
    [1, 2, 3],
    [4, 5, 6]
]
result2 = intersection_of_sorted_arrays(arrays2)
print(result2) # Output: []

arrays3 = [
    [1, 2, 3, 4, 5],
    [1, 2, 5, 7, 9],
    [1, 3, 4, 5, 8]
]

result3 = intersection_of_sorted_arrays(arrays3)
print(result3) #Output: [1, 5]
```

**Explanation:**

1.  **`intersection_of_sorted_arrays(arrays)`:**
    *   Handles the main logic for finding the intersection of multiple arrays.
    *   If the input list of arrays is empty, it returns an empty list.
    *   If there is only one array in the list, it removes duplicate elements and sorts the array.
    *   It initializes the `intersection` list with the elements of the first array.
    *   It iterates through the remaining arrays in the list, updating the `intersection` by finding the common elements between the current `intersection` and the next array using the `find_intersection_of_two_sorted_arrays` helper function.
    *   Finally, it converts the `intersection` list to a set to remove duplicate elements, sorts the set, and returns the result as a list.

2.  **`find_intersection_of_two_sorted_arrays(arr1, arr2)`:**
    *   This is a helper function that finds the intersection of two sorted arrays `arr1` and `arr2`.
    *   It uses two pointers `i` and `j` to iterate through the arrays simultaneously.
    *   If `arr1[i]` and `arr2[j]` are equal, it means that the element is present in both arrays, so it is added to the `result` list, and both pointers are incremented.
    *   If `arr1[i]` is less than `arr2[j]`, it means that `arr1[i]` is not present in `arr2`, so the `i` pointer is incremented.
    *   If `arr1[i]` is greater than `arr2[j]`, it means that `arr2[j]` is not present in `arr1`, so the `j` pointer is incremented.
    *   The loop continues until either `i` or `j` reaches the end of their respective arrays.

**Time and Space Complexity:**

*   **Time Complexity:** O(N * M), where N is the total number of arrays, and M is the average length of the arrays.  The `find_intersection_of_two_sorted_arrays` function has a time complexity of O(min(len(arr1), len(arr2))), and it is called N-1 times.  Conversion to set and sorting contributes O(K log K) where K is the final number of elements in the intersection. This could be less significant than N*M if the intersection is relatively small.
*   **Space Complexity:** O(K), where K is the number of elements in the intersection. This is because we store the intersection in a new list.  In the worst case, if all arrays have the same elements, the space complexity could be O(min(length of input arrays)).
