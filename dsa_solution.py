Okay, here's a problem and a Python solution:

**Problem:**

**Task Scheduler with Cooling Period**

You are given a list of tasks represented by characters. Each task can be done in one unit of time. You are also given a non-negative integer `n`, which represents the cooling period between two same tasks. During the cooling period, the CPU can either be idle or perform a different task.

Write a function that calculates the minimum number of time units required to finish all given tasks while adhering to the cooling period constraint.

**Example:**

```
tasks = ["A","A","A","B","B","B"]
n = 2
```

**Explanation:**

One possible schedule is: A -> B -> idle -> A -> B -> idle -> A -> B.
Therefore, the minimum number of time units required is 8.

**Python Solution:**

```python
from collections import Counter

def leastInterval(tasks, n):
    """
    Calculates the least number of intervals to complete all tasks with cooling period.

    Args:
        tasks: A list of characters representing tasks.
        n: The cooling period between the same tasks.

    Returns:
        The minimum number of time units required.
    """
    if not tasks:
        return 0

    task_counts = Counter(tasks)
    max_count = max(task_counts.values())
    max_tasks = sum(1 for count in task_counts.values() if count == max_count)

    # The core idea: We fill the schedule with the most frequent task,
    # leaving "idle slots" between occurrences.  The math handles edge cases.
    result = max((max_count - 1) * (n + 1) + max_tasks, len(tasks))
    return result

# Example usage:
tasks = ["A","A","A","B","B","B"]
n = 2
result = leastInterval(tasks, n)
print(f"Minimum time units: {result}")  # Output: 8

tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2
result = leastInterval(tasks, n)
print(f"Minimum time units: {result}")  # Output: 12

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
result = leastInterval(tasks, n)
print(f"Minimum time units: {result}")  # Output: 16

tasks = ["A","A","B","B"]
n = 0
result = leastInterval(tasks, n)
print(f"Minimum time units: {result}") # Output 4
```

**Explanation:**

1. **Count Task Frequencies:** We use `Counter` from the `collections` module to count the frequency of each task.

2. **Find the Most Frequent Task:** We determine the maximum frequency (`max_count`) and the number of tasks that have this maximum frequency (`max_tasks`).

3. **Calculate the Minimum Time Units:**
   - The core logic is based on filling the schedule with the most frequent tasks and using idle slots to satisfy the cooling period.  The formula `(max_count - 1) * (n + 1) + max_tasks` calculates the ideal schedule length based on the most frequent task and the cooling period.  `(max_count - 1)` is the number of gaps between the occurrences of the most frequent task.  Each gap needs to be at least of length `n+1` (including the task itself).  `max_tasks` is added to handle the last occurrences of tasks with the maximum count.
   - `max(..., len(tasks))` handles the cases where the idle slots aren't actually needed because there are enough different tasks to fill them. In such cases, the minimum time is simply the number of tasks.

**Key Concepts:**

*   **Greedy Approach:** The solution implicitly uses a greedy approach by prioritizing the most frequent task.  It aims to schedule these tasks as early as possible, forcing the CPU to idle or switch to other tasks.
*   **Counting:** The `Counter` class is very useful for counting occurrences of items in a list.
*   **Mathematical Formula:**  The critical part of the solution is the formula to calculate the minimum number of time units, which is based on the task frequencies and the cooling period.  Understanding the derivation of this formula is essential to grasp the algorithm.

**Time Complexity:**

*   O(T), where T is the number of tasks. This is dominated by the `Counter` operation.

**Space Complexity:**

*   O(k), where k is the number of unique tasks. This is due to the `Counter` object.  In the worst case, `k` can be equal to `T`, but it's usually much smaller.