import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if numCourses <= 1:
            return [i for i in range(numCourses)]
        vertices = numCourses
        edges = prerequisites

        # initialize graph
        in_degree = {i: 0 for i in range(vertices)}
        graph = {i: [] for i in range(vertices)}

        # create graph
        for child, parent in edges:
            in_degree[child] += 1
            graph[parent].append(child)

        # adding courses that does not require prerequisite
        sources = collections.deque()
        for key, val in in_degree.items():
            if val == 0:
                sources.append(key)

        res = []
        while sources:
            vertex = sources.popleft()
            res.append(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)
        if len(res) != numCourses:
            return []
        return res


a = Solution()
a.findOrder(1, [])
