Okay, here's a randomly generated DSA problem and a Python solution.

**Problem:**

**Merge Intervals**

Given a list of intervals, where each interval is represented as a pair of integers `[start, end]`, merge all overlapping intervals and return a list of non-overlapping intervals that cover all the intervals in the input.

**Example:**

*   **Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`
*   **Output:** `[[1,6],[8,10],[15,18]]`

**Explanation:**
Intervals `[1,3]` and `[2,6]` overlap, so they are merged into `[1,6]`.

**Python Code Solution:**

```python
def merge_intervals(intervals):
    """
    Merges overlapping intervals.

    Args:
        intervals: A list of intervals (lists of two integers).

    Returns:
        A list of merged intervals.
    """

    if not intervals:
        return []

    # Sort the intervals by start time. This is crucial for the algorithm to work.
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the list of merged intervals is empty or if the current
        # interval does not overlap with the last interval, simply append it.
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Otherwise, there is overlap, so we merge the current interval
            # with the last interval.  We update the end of the last interval
            # to be the maximum of the two ends.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
merged_intervals = merge_intervals(intervals)
print(f"Merged intervals: {merged_intervals}")  # Output: Merged intervals: [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1,4],[4,5]]
merged_intervals2 = merge_intervals(intervals2)
print(f"Merged intervals: {merged_intervals2}") # Output: Merged intervals: [[1, 5]]

intervals3 = [[1,4],[0,4]]
merged_intervals3 = merge_intervals(intervals3)
print(f"Merged intervals: {merged_intervals3}") # Output: Merged intervals: [[0, 4]]

intervals4 = [[1,4],[0,0]]
merged_intervals4 = merge_intervals(intervals4)
print(f"Merged intervals: {merged_intervals4}") # Output: Merged intervals: [[0, 0], [1, 4]]

intervals5 = [[1,4],[0,2],[3,5]]
merged_intervals5 = merge_intervals(intervals5)
print(f"Merged intervals: {merged_intervals5}") # Output: Merged intervals: [[0, 5]]
```

**Explanation:**

1.  **Sort Intervals:** The most important step is to sort the intervals based on their start times.  This allows us to process them in a logical order and easily check for overlaps.  We use `intervals.sort(key=lambda x: x[0])` to sort in place.

2.  **Iterate and Merge:**  We iterate through the sorted intervals and maintain a `merged` list to store the non-overlapping intervals.

3.  **Overlap Check:** For each interval, we check if it overlaps with the last interval in the `merged` list.  There are two scenarios:

    *   **No Overlap:** If the current interval's start time is greater than the end time of the last interval in `merged`, then there's no overlap.  We simply append the current interval to `merged`.
    *   **Overlap:** If there *is* overlap, we merge the intervals.  We update the end time of the last interval in `merged` to be the maximum of its current end time and the end time of the current interval.  This effectively combines the two overlapping intervals.

4.  **Return Merged:** After iterating through all the intervals, the `merged` list contains the non-overlapping intervals that cover the original intervals.

**Time and Space Complexity:**

*   **Time Complexity:** O(n log n) due to the sorting step.  The rest of the algorithm is O(n).
*   **Space Complexity:** O(n) in the worst case, where no intervals overlap, and we store all the original intervals in the `merged` list. In the best case (high overlap), it could be O(1) beyond the input list, if the `merged` list is significantly smaller than the input.
