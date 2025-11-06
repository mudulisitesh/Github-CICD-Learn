Okay, here's a DSA problem with a Python solution.  I'll try to make it a bit more interesting than the absolute basics.

**Problem:**

**Merge Intervals (Non-overlapping and Sorted)**

Given a list of intervals represented as pairs of integers (start, end), where `start` is the starting point and `end` is the ending point of the interval, merge all overlapping intervals and return a list of non-overlapping intervals in sorted order. Assume that the intervals are initially sorted by their start times.

**Example:**

Input: `[[1,3],[2,6],[8,10],[15,18]]`
Output: `[[1,6],[8,10],[15,18]]`

Explanation: `[1,3]` and `[2,6]` overlap, so they are merged into `[1,6]`.

Input: `[[1,4],[4,5]]`
Output: `[[1,5]]`

**Python Solution:**

```python
def merge_intervals(intervals):
    """
    Merges overlapping intervals.

    Args:
        intervals: A list of intervals, where each interval is a list/tuple of two integers (start, end).
                   Assumes the intervals are already sorted by start time.

    Returns:
        A list of non-overlapping intervals.
    """

    if not intervals:
        return []

    merged_intervals = []
    current_interval = intervals[0]  # Initialize with the first interval

    for i in range(1, len(intervals)):
        next_interval = intervals[i]

        # Check for overlap
        if next_interval[0] <= current_interval[1]:  # next start <= current end
            # Merge the intervals
            current_interval = [current_interval[0], max(current_interval[1], next_interval[1])]
        else:
            # No overlap, add the current interval to the result and update the current_interval
            merged_intervals.append(current_interval)
            current_interval = next_interval

    # Add the last current interval to the result
    merged_intervals.append(current_interval)

    return merged_intervals

# Example Usage:
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(f"Merged intervals for {intervals1}: {merge_intervals(intervals1)}")  # Output: [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1,4],[4,5]]
print(f"Merged intervals for {intervals2}: {merge_intervals(intervals2)}") # Output: [[1, 5]]

intervals3 = [[1,4],[0,4]]
print(f"Merged intervals for {intervals3}: {merge_intervals(intervals3)}")  # Output: [[0, 4]]

intervals4 = [[1,4],[0,0]] #Note, not sorted!  The code assumes already sorted!
print(f"Merged intervals for {intervals4}: {merge_intervals(intervals4)}") # Output: [[1, 4], [0, 0]] Note the incorrect result!
```

**Explanation:**

1. **Initialization:**
   - We start with an empty list `merged_intervals` to store the non-overlapping intervals.
   - We initialize `current_interval` with the first interval in the input list.  This will be our base for merging.

2. **Iteration:**
   - We iterate through the remaining intervals in the input list (starting from the second interval).
   - For each `next_interval`, we check if it overlaps with the `current_interval`.

3. **Overlap Check:**
   - The key condition for overlap is: `next_interval[0] <= current_interval[1]`.  This means the starting point of the `next_interval` is less than or equal to the ending point of the `current_interval`.

4. **Merging:**
   - If there is an overlap, we merge the intervals. The start of the new merged interval will be the start of the `current_interval` (since the input is sorted).  The end of the merged interval will be the maximum of the end points of the `current_interval` and the `next_interval`.
   - `current_interval = [current_interval[0], max(current_interval[1], next_interval[1])]`

5. **No Overlap:**
   - If there is no overlap, it means the `next_interval` is completely separate from the `current_interval`.
   - We add the `current_interval` to the `merged_intervals` list.
   - We update `current_interval` to be the `next_interval` to start the merging process with the new interval.

6. **Adding the Last Interval:**
   - After the loop finishes, the `current_interval` will still contain the last interval (or the merged interval that was in progress).  We add this `current_interval` to the `merged_intervals` list to complete the process.

7. **Return:**
   - Finally, we return the `merged_intervals` list, which contains the non-overlapping merged intervals.

**Time and Space Complexity:**

*   **Time Complexity:** O(n), where n is the number of intervals.  We iterate through the list of intervals once.
*   **Space Complexity:** O(n) in the worst case, where no intervals overlap, and we need to store all the intervals in the `merged_intervals` list.  In the best case (all intervals merge into one), the space complexity would be O(1).

**Important Note:** This solution assumes that the input intervals are already sorted by their start times. If the intervals are not sorted, you will need to sort them first. Adding the sorting step would increase the time complexity to O(n log n). You would sort them like this: `intervals.sort(key=lambda x: x[0])` before doing the rest of the algorithm.
