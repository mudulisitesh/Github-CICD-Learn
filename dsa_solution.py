Okay, here's a DSA problem and a Python solution:

**Problem:**

**Nearest Smaller Elements**

Given an array of integers `nums`, for each element `nums[i]`, find the nearest smaller element to its left. If there is no smaller element to the left, consider the nearest smaller element as -1. Return an array of the nearest smaller elements for each element in the input array.

**Example:**

```
Input: nums = [4, 5, 2, 10, 8]
Output: [-1, 4, -1, 2, 2]
```

**Explanation:**

*   For `nums[0] = 4`, there is no smaller element to its left. Hence, -1.
*   For `nums[1] = 5`, the nearest smaller element to its left is 4.
*   For `nums[2] = 2`, there is no smaller element to its left. Hence, -1.
*   For `nums[3] = 10`, the nearest smaller element to its left is 2.
*   For `nums[4] = 8`, the nearest smaller element to its left is 2.

**Python Solution:**

```python
def nearest_smaller_elements(nums):
    """
    Finds the nearest smaller element to the left for each element in the input array.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers representing the nearest smaller elements.
    """

    result = []
    stack = []  # Use a stack to keep track of potentially smaller elements

    for num in nums:
        while stack and stack[-1] >= num:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(num)

    return result

# Example usage:
nums = [4, 5, 2, 10, 8]
output = nearest_smaller_elements(nums)
print(output)  # Output: [-1, 4, -1, 2, 2]

nums2 = [1, 3, 2, 4]
output2 = nearest_smaller_elements(nums2)
print(output2) # Output: [-1, 1, 1, 2]

nums3 = [5,4,3,2,1]
output3 = nearest_smaller_elements(nums3)
print(output3) #Output: [-1, -1, -1, -1, -1]
```

**Explanation of the Solution:**

1.  **Stack Data Structure:**  We use a stack to efficiently keep track of the elements that could potentially be the nearest smaller element to the left for future elements in the array.  The stack will maintain a decreasing order of elements from bottom to top.

2.  **Iteration:**  We iterate through the `nums` array.

3.  **Stack Maintenance:**
    *   `while stack and stack[-1] >= num:`:  Before considering the current number `num`, we pop elements from the stack as long as the top of the stack is greater than or equal to `num`.  This is because elements in the stack that are greater than or equal to the current `num` cannot be the nearest smaller element for any element to the right of the current position. We want to maintain the decreasing order in the stack.
    *   `if not stack:`: If the stack is empty after the popping, it means there are no smaller elements to the left of `num`. So we append -1 to the `result`.
    *   `else:`: If the stack is not empty, the top of the stack `stack[-1]` is the nearest smaller element to the left of `num`. So we append it to the `result`.
    *   `stack.append(num)`: Finally, we push the current number `num` onto the stack.

4.  **Return:**  After iterating through the entire array, we return the `result` array containing the nearest smaller elements.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the length of the input array `nums`. Although there is a `while` loop inside the `for` loop, each element is pushed onto the stack and popped from the stack at most once. Therefore, the amortized time complexity is O(n).
*   **Space Complexity:** O(n), because in the worst case, the stack can store all the elements of the input array.
