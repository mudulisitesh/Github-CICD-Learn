Okay, here's a DSA problem along with a Python solution.

**Problem:**

**Task Scheduler with Cooling Period**

You are given a list of tasks represented by characters (A to Z), and a non-negative integer `n` representing the cooling period between two same tasks.  Each task can be done in one unit of time.  For each unit of time, the CPU can either process a task or be idle.

Your task is to find the minimum number of units of time required to complete all the tasks.

**Example:**

```
tasks = ["A","A","A","B","B","B"]
n = 2

Output: 8

Explanation:
One possible schedule is: A -> B -> idle -> A -> B -> idle -> A -> B.
```

**Code Solution (Python):**

```python
import heapq

def least_interval(tasks, n):
    """
    Calculates the minimum time to complete tasks with a cooling period.

    Args:
        tasks: A list of task characters.
        n: The cooling period between the same tasks.

    Returns:
        The minimum number of units of time required to complete the tasks.
    """

    task_counts = {}
    for task in tasks:
        task_counts[task] = task_counts.get(task, 0) + 1

    # Use a max heap to store the counts (negated to simulate max heap).
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)

    time = 0
    while max_heap:
        # List to store tasks that need to be added back to the heap.
        temp_tasks = []
        # Process 'n+1' tasks, or until the heap is empty.
        for _ in range(n + 1):
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1 # Simulate processing the task (decrement count).
                if count < 0: # If the task is not yet finished, add it back.
                    temp_tasks.append(count)
            if not max_heap and not temp_tasks: # optimization: stop if heap is empty
                break  # No more tasks to execute

        # Add the tasks back to the heap that need more processing.
        for task in temp_tasks:
            heapq.heappush(max_heap, task)

    return time


# Example usage:
tasks = ["A","A","A","B","B","B"]
n = 2
print(f"Minimum time required: {least_interval(tasks, n)}")  # Output: 8

tasks = ["A","A","A","B","B","B", "C", "C"]
n = 2
print(f"Minimum time required: {least_interval(tasks, n)}")  # Output: 10

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(f"Minimum time required: {least_interval(tasks, n)}") #Output: 16
```

**Explanation:**

1. **Count Task Frequencies:**  We start by counting the occurrences of each task using a dictionary `task_counts`.

2. **Max Heap:**  We use a max heap (implemented with `heapq` and negated values) to keep track of the tasks with the highest frequencies.  The task with the highest frequency will be processed first to minimize idle time.

3. **Processing in Rounds:**
   - The main `while` loop continues as long as there are tasks in the heap.
   - In each iteration, we try to process `n + 1` tasks (or fewer if there are fewer than `n + 1` tasks available).  This simulates the cooling period.
   - We keep track of tasks that are processed but not yet finished in the `temp_tasks` list.
   - After processing `n + 1` tasks, we add the tasks from `temp_tasks` back into the max heap.  It's important that the loop breaks, if no more tasks are left.

4. **Time Calculation:**  The `time` variable keeps track of the total units of time required.  We increment it in each inner loop iteration to account for processing a task or being idle.

**Time and Space Complexity:**

- **Time Complexity:** O(N + M log M), where N is the number of tasks and M is the number of unique task types.  O(N) to count task frequencies, and O(M log M) for heap operations.
- **Space Complexity:** O(M), where M is the number of unique task types.  This is due to the `task_counts` dictionary and the `max_heap`.
**Why this approach works:**

The key idea is to prioritize the tasks with the highest frequencies. By processing the most frequent tasks as early as possible, we maximize the CPU's utilization and minimize the number of idle slots.  The heap ensures we always have access to the most frequent task currently available after the cooling period.
