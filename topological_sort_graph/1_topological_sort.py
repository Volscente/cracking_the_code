"""
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that
for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:
Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
"""

from collections import deque


def topological_sort(vertices, edges):
    """
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    :param vertices:
    :param edges:
    :return:
    """

    sorted_list = []

    # Init dicts
    # O(V)
    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    # Populate dicts
    # O(E)
    for edge in edges:
        parent, child = edge[0], edge[1]
        in_degree[child] += 1
        graph[parent].append(child)

    # Init source
    sources = deque()
    # O(V)
    for node in in_degree:
        if in_degree[node] == 0:
            sources.append(node)

    # BFS
    # O(V + E)
    while sources:

        node = sources.popleft()
        sorted_list.append(node)

        for child in graph[node]:
            in_degree[child] -= 1

            if in_degree[child] == 0:
                sources.append(child)

    # Avoid Directed Acyclic Graph
    if len(sorted_list) != vertices:
        return []

    return sorted_list


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
