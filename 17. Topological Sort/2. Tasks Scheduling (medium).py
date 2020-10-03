# Problem Statement
# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be
# completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if
# it is possible to schedule all the tasks.

from collections import deque


def is_scheduling_possible(tasks, prerequisites):
    """
    Time: O(V+E)
    Space: O(V+E) storing all of the edges for each vertex in an adjacency list.
    """
    sorted_order = []
    if tasks <= 0:
        return False

    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for parent, child in prerequisites:
        in_degree[child] += 1
        graph[parent].append(child)

    sources = deque()
    for key, value in in_degree.items():
        if value == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == tasks


def main():
    # print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    # print("Is scheduling possible: " + str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
