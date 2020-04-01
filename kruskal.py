def kruskal(graph):
    assert type(graph)==dict

    nodes = graph.keys()
    visited = set()
    path = []
    next = None

    while len(visited) < len(nodes):
        distance = float('inf')
        for s in nodes:
            for d in nodes:
                if s in visited and d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d

        path.append((pre, next))
        visited.add(pre)
        visited.add(next)

    return path

graph_dict = {  "v1": {"v1": 0, "v2": 1, "v3": 3, "v4": 999, "v5": 999},
                    "v2": {"v1": 1, "v2": 0, "v3": 3, "v4": 6, "v5": 999},
                    "v3": {"v1": 3, "v2": 3, "v3": 0, "v4": 4, "v5": 2},
                    "v4": {"v1": 999, "v2": 6, "v3": 4, "v4": 0, "v5": 5},
                    "v5": {"v1": 999, "v2": 999, "v3": 2, "v4": 5, "v5": 0},
    }

path = kruskal(graph_dict)
print(path)