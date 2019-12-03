def prim(graph, root):
    assert type(graph) == dict

    # nodes = graph.keys()
    nodes = list(graph)
    nodes.remove(root)

    visited = [root]
    path = []
    next = None

    while nodes:
        distance = float('inf')
        for s in visited:
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d
        path.append((pre, next))
        visited.append(next)
        nodes.remove(next)

    return path


if __name__ == '__main__':
    graph_dict = {  "v1": {"v1": 0, "v2": 1, "v3": 3, "v4": 999, "v5": 999},
                    "v2": {"v1": 1, "v2": 0, "v3": 3, "v4": 6, "v5": 999},
                    "v3": {"v1": 3, "v2": 3, "v3": 0, "v4": 4, "v5": 2},
                    "v4": {"v1": 999, "v2": 6, "v3": 4, "v4": 0, "v5": 5},
                    "v5": {"v1": 999, "v2": 999, "v3": 2, "v4": 5, "v5": 0},
                  }

    path = prim(graph_dict, 'v1')
    print(path)