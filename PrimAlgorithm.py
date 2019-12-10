graph_dict = {
    "v1": {"v1": 0, "v2": 1, "v3": 3, "v4": 999, "v5": 999},
    "v2": {"v1": 1, "v2": 0, "v3": 3, "v4": 6, "v5": 999},
    "v3": {"v1": 3, "v2": 3, "v3": 0, "v4": 4, "v5": 2},
    "v4": {"v1": 999, "v2": 6, "v3": 4, "v4": 0, "v5": 5},
    "v5": {"v1": 999, "v2": 999, "v3": 2, "v4": 5, "v5": 0},
}

def prim (graph) :
    path = []
    visited = ['v1']
    nodes = list(graph)
    nodes.remove('v1')
    next = None
    while nodes :
        distance = 999
        for i in visited :
            for j in graph[i] :
                if i == j or j in visited:
                    continue
                if graph[i][j] < distance and graph[i][j] > 0:
                    distance = graph[i][j]
                    pre = i
                    next = j
        path.append((pre, next))
        visited.append(next)
        nodes.remove(next)
    return path
print(prim(graph_dict))