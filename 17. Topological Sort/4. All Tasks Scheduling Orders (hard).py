# Problem Statement
# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be
# completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a
# method to print all possible ordering of tasks meeting all prerequisites.

from collections import deque


def print_orders(tasks, prerequisites):
    """
    Time: O(V!∗E) N! combinations for ‘N’ numbers, ‘V’ is the total number of tasks and ‘E’ is the total prerequisites.
    Space: O(V!∗E)
    """
    sorted_order = []
    if tasks <= 0:
        return False
    # a. Initialize the graph
    in_degree = {i: 0 for i in range(tasks)}  # count of incoming edges
    graph = {i: [] for i in range(tasks)}  # adjacency list graph
    # b. Build the graph
    for parent, child in prerequisites:
        graph[parent].append(child)  # put the child into it's parent's list
        in_degree[child] += 1  # to see how many prerequisite
    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)
    print_all_topological_sorts(graph, in_degree, sources, sorted_order)


def print_all_topological_sorts(graph, in_degree, sources, sorted_order):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = deque(sources)  # make a copy of sources
            # only remove the current source, all other sources should remain in the qu
            sources_for_next_call.remove(vertex)
            # get the node's children to decrement their in-degrees
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)
            # recursive call to print other orderings from the remaining (and new) sour
            print_all_topological_sorts(graph, in_degree, sources_for_next_call, sorted_order)
            # backtrack, remove the vertex from the sorted order and put all of its chi
            # the next source instead of the current vertex
            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1
    # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency bet
    # we have not processed all the tasks in this recursive call
    if len(sorted_order) == len(in_degree):
        print(sorted_order)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])
    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
