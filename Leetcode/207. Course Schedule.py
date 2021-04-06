class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True
        vertices = numCourses
        edges = prerequisites
        sorted_order = []

        # initialize the graph
        in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
        graph = {i: [] for i in range(vertices)}  # adjacency list graph

        # build the graph
        for parent, child in edges:
            graph[parent].append(child)
            in_degree[child] += 1

        # find all sources with 0 dependencies
        sources = collections.deque()
        for key, value in in_degree.items():
            if value == 0:
                sources.append(key)

        # for each source, add it to the sorted order, then subtract one and add it to process if in-degree becomes zero
        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        if len(sorted_order) != vertices:
            return False
        return True
