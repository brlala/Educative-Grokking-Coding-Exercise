import heapq


def find_maximized_capital(max_projects, current_capital, project_profits, project_capital):
    heap = []
    projects = sorted(zip(project_profits, project_capital), key=lambda project: project[1])
    project = 0
    while max_projects:
        while project < len(projects) and projects[project][1] <= current_capital:
            heapq.heappush(heap, -projects[project][0])
            project += 1
        if heap:
            current_capital -= heapq.heappop(heap)
        max_projects -= 1
    return current_capital


print(find_maximized_capital(2, 0, [1, 5, 3], [0, 0, 1]))
