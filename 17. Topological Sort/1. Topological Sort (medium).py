# Problem Statement
# Given a directed graph, find the topological ordering of its vertices.

from collections import deque


def topological_sort(vertices, edges):
    """
    Time: O(V+E)
    Space: O(V+E) storing all of the edges for each vertex in an adjacency list.
    """
    sorted_order = []
    if vertices <= 0:
        return sorted_order
    # a. Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # b. Build the graph
    for parent, child in edges:
        graph[parent].append(child)  # put the child into parent's list
        in_degree[child] += 1  # increment child's in-degree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key, value in in_degree.items():
        if value == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of it
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)  # with no more child
        for child in graph[vertex]:  # get the node's children to decrement their in-degree
            in_degree[child] -= 1  # how many arrows pointing to the node
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []
    return sorted_order


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
