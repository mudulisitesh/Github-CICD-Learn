Okay, here's a DSA problem and a corresponding Python solution.

**Problem:**

**Merge Overlapping Intervals**

Given a list of intervals, where each interval is represented as a pair of integers `[start, end]`, merge all overlapping intervals and return a list of non-overlapping intervals that cover the same range.

**Example:**

Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`
Output: `[[1,6],[8,10],[15,18]]`
Explanation: Intervals `[1,3]` and `[2,6]` overlap, so they are merged into `[1,6]`.

Input: `intervals = [[1,4],[4,5]]`
Output: `[[1,5]]`
Explanation: Intervals `[1,4]` and `[4,5]` are considered overlapping.

**Python Solution:**

```python
def merge_intervals(intervals):
    """
    Merges overlapping intervals in a list.

    Args:
        intervals: A list of intervals, where each interval is a list of two integers [start, end].

    Returns:
        A list of non-overlapping intervals that cover the same range.
    """

    if not intervals:
        return []

    # Sort the intervals by the start time.  Crucial step.
    intervals.sort(key=lambda x: x[0])  # Sort by the first element of each sublist

    merged = []
    for interval in intervals:
        # If the list of merged intervals is empty or if the current
        # interval does not overlap with the last interval, simply append it.
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Otherwise, there is overlap, so we merge the current interval
            # with the last interval.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example Usage
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(f"Input: {intervals1}, Output: {merge_intervals(intervals1)}")  # Output: [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1,4],[4,5]]
print(f"Input: {intervals2}, Output: {merge_intervals(intervals2)}")  # Output: [[1, 5]]

intervals3 = [[1,4],[0,4]]
print(f"Input: {intervals3}, Output: {merge_intervals(intervals3)}") # Output: [[0, 4]]

intervals4 = [[1,4],[0,0]]
print(f"Input: {intervals4}, Output: {merge_intervals(intervals4)}") # Output: [[0, 0], [1, 4]]
```

**Explanation:**

1. **Handle Empty Input:**  The function first checks if the input list of intervals is empty. If it is, it returns an empty list.

2. **Sort Intervals:** The most important step is to sort the intervals based on their starting times.  This allows us to iterate through the intervals in a predictable order and easily determine if they overlap. The `intervals.sort(key=lambda x: x[0])` line sorts the list in place.  The `lambda x: x[0]` is a small anonymous function that extracts the first element (the start time) of each interval for sorting.

3. **Iterate and Merge:**
   - We create an empty list `merged` to store the non-overlapping intervals.
   - We iterate through the sorted intervals.
   - For each `interval`, we check if it overlaps with the last interval in the `merged` list.
     - **No Overlap:** If `merged` is empty or the current interval's start time is greater than the end time of the last interval in `merged` ( `interval[0] > merged[-1][1]` ), then there's no overlap. We simply append the current `interval` to `merged`.
     - **Overlap:** If there is overlap (the current interval's start time is less than or equal to the end time of the last interval in `merged`), we merge the intervals. We update the end time of the last interval in `merged` to be the maximum of its current end time and the current interval's end time (`merged[-1][1] = max(merged[-1][1], interval[1])`).  This effectively extends the last interval to cover the overlapping portion.

4. **Return Result:** Finally, we return the `merged` list, which contains the non-overlapping intervals.

**Time and Space Complexity:**

* **Time Complexity:** O(n log n) due to the sorting step. The rest of the algorithm takes O(n) time.
* **Space Complexity:** O(n) in the worst case, where no intervals overlap, and the `merged` list stores all the input intervals.  In other cases, it can be less than O(n).
