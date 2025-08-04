Okay, here's a random DSA problem and a Python solution:

**Problem:**

**Merge Intervals**

Given a collection of intervals represented as a list of lists, where each inner list contains the start and end points of an interval (e.g., `[[1,3], [2,6], [8,10], [15,18]]`), merge all overlapping intervals and return a list of non-overlapping intervals that cover all the intervals in the input.

**Example:**

Input: `[[1,3], [2,6], [8,10], [15,18]]`
Output: `[[1,6], [8,10], [15,18]]`

Explanation: The intervals `[1,3]` and `[2,6]` overlap, so they are merged into `[1,6]`.

Input: `[[1,4],[4,5]]`
Output: `[[1,5]]`

**Python Solution:**

```python
def merge_intervals(intervals):
    """
    Merges overlapping intervals in a list of intervals.

    Args:
        intervals: A list of intervals, where each interval is a list [start, end].

    Returns:
        A list of merged non-overlapping intervals.
    """

    if not intervals:
        return []

    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the list of merged intervals is empty or if the current
        # interval does not overlap with the last interval, simply append it.
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Otherwise, there is overlap, so we merge the current and last
            # intervals.  The end time will be the max of both interval's ends.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example Usage:
intervals1 = [[1,3], [2,6], [8,10], [15,18]]
print(f"Input: {intervals1}, Output: {merge_intervals(intervals1)}") # Output: [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1,4],[4,5]]
print(f"Input: {intervals2}, Output: {merge_intervals(intervals2)}") # Output: [[1, 5]]

intervals3 = [[1,4],[0,4]]
print(f"Input: {intervals3}, Output: {merge_intervals(intervals3)}") # Output: [[0, 4]]

intervals4 = [[1,4],[0,0]]
print(f"Input: {intervals4}, Output: {merge_intervals(intervals4)}") # Output: [[0, 0], [1, 4]]

intervals5 = [[1,4],[0,2],[3,5]]
print(f"Input: {intervals5}, Output: {merge_intervals(intervals5)}") # Output: [[0, 5]]

intervals6 = [[7,9],[6,10],[4,5],[1,3],[2,4]]
print(f"Input: {intervals6}, Output: {merge_intervals(intervals6)}") # Output: [[1, 5], [6, 10]]
```

**Explanation:**

1. **Sort:** The intervals are sorted based on their starting points.  This is crucial for efficiently merging overlapping intervals.

2. **Iterate and Merge:**
   - We maintain a `merged` list to store the non-overlapping intervals.
   - For each interval in the sorted `intervals` list:
     - If `merged` is empty or the current interval doesn't overlap with the last interval in `merged`, we simply append the current interval to `merged`.  No overlap means that the current interval's start time is greater than the last interval's end time.
     - If there's overlap, we update the end time of the last interval in `merged` to be the maximum of the two intervals' end times.

**Time and Space Complexity:**

- **Time Complexity:** O(n log n) primarily due to the sorting step. The rest of the algorithm is O(n).
- **Space Complexity:** O(n) in the worst case, where no intervals overlap, and the `merged` list contains all the original intervals.  In many cases, it will be less than O(n) because intervals are merged.
