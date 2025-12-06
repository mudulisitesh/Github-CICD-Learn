Okay, here's a DSA problem and a Python solution:

**Problem:**

**Meeting Rooms**

Given an array of meeting time intervals where `intervals[i] = [starti, endi]`, determine if a person could attend all meetings.

**Example 1:**

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

**Example 2:**

```
Input: intervals = [[7,10],[2,4]]
Output: true
```

**Explanation:**

The problem asks to determine if any meeting intervals overlap.  If there are overlaps, it means a person can't attend all meetings. The key is to sort the intervals by start time and then check for overlaps sequentially.

**Python Code:**

```python
def can_attend_all_meetings(intervals):
    """
    Determines if a person can attend all meetings given a list of meeting time intervals.

    Args:
        intervals: A list of lists, where each inner list represents a meeting interval [start, end].

    Returns:
        True if the person can attend all meetings, False otherwise.
    """

    if not intervals:
        return True  # No meetings, so they can attend all

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])  # sorting

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]: # checking if current meeting start time is less than previous meeting end time
            return False  # Overlap found

    return True  # No overlaps found


# Example Usage:
intervals1 = [[0,30],[5,10],[15,20]]
print(f"Can attend all meetings (Example 1): {can_attend_all_meetings(intervals1)}")  # Output: False

intervals2 = [[7,10],[2,4]]
print(f"Can attend all meetings (Example 2): {can_attend_all_meetings(intervals2)}")  # Output: True

intervals3 = [[1,3],[6,8],[3,5],[9,12]]
print(f"Can attend all meetings (Example 3): {can_attend_all_meetings(intervals3)}") #Output: False
```

**Explanation of the Code:**

1.  **Handle Empty Input:** The code first checks if the `intervals` list is empty. If it is, it means there are no meetings, so the person can attend all of them, and `True` is returned.

2.  **Sort by Start Time:** The `intervals.sort(key=lambda x: x[0])` line sorts the list of intervals based on their starting times.  The `key=lambda x: x[0]` is a lambda function that tells the `sort` method to use the first element of each inner list (the start time) as the sorting key. Sorting is crucial for efficiently detecting overlaps.

3.  **Check for Overlaps:** The code then iterates through the sorted intervals, starting from the second interval (index 1).  For each interval `i`, it compares its start time (`intervals[i][0]`) with the end time of the previous interval (`intervals[i-1][1]`).

4.  **Overlap Condition:** If the start time of the current interval is less than the end time of the previous interval (`intervals[i][0] < intervals[i-1][1]`), it means there is an overlap. In this case, the function immediately returns `False`.

5.  **No Overlaps:** If the loop completes without finding any overlaps, it means the person can attend all meetings, and the function returns `True`.

**Time and Space Complexity:**

*   **Time Complexity:** O(n log n), primarily due to the sorting step.  The rest of the code iterates through the list of intervals once, which takes O(n) time.  Sorting dominates the time complexity.
*   **Space Complexity:** O(1) or O(n) depending on the sorting algorithm used by Python's `sort()` function. In most implementations, it's either in-place (O(1)) or uses O(log n) auxiliary space. However, in the worst case, it could be O(n).  The rest of the code uses a constant amount of extra space.
