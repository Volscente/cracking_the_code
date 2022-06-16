"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example 1:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs
to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2]

Example 2:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.

Example 3:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
"""

from collections import deque


def is_scheduling_possible(tasks, prerequisites):

    # O(V)
    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    traversal_list = []

    # O(E)
    for edge in prerequisites:
        parent, child = edge[0], edge[1]
        in_degree[child] += 1
        graph[parent].append(child)

    sources = deque()

    # O(E)
    for node in in_degree:
        if in_degree[node] == 0:
            sources.append(node)

    # O(V + E)
    while sources:
        source = sources.popleft()
        traversal_list.append(source)

        for child in graph[source]:
            in_degree[child] -= 1

            if in_degree[child] == 0:
                sources.append(child)

    return len(traversal_list) == tasks


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()


