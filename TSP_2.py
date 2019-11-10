INF = 10000
dist = [[0, 2, 9, INF],
        [1, 0, 6, 4],
        [INF, 7, 0, 8],
        [6, 3, INF, 0]]
visited = 1 << 4
path = [0]
cost = 0

def tsp (path, visited, cost) :
    N = len(dist)


    VISITED_ALL = (1 << N) - 1

    if len(path) == N :
        return cost + dist[path[-1]][0]
    ret = 100000

    for i in range(N) :
        if visited[i] != 1 :
            visited[i] = 1
            path.append(i)
            cost += dist[path[-1]][i]
            ret = min(ret, tsp(path, visited, cost))
            visited[i] = 0
            path.pop()
    print(visited)
    print(path)
    return ret

print(tsp(path, visited, cost))