INF = 10000
dist = [[0, 2, 9, INF],
        [1, 0, 6, 4],
        [INF, 7, 0, 8],
        [6, 3, INF, 0]]

N = len(dist)
VISITED_ALL = (1 << N)-1
visited = 1 << 1
path = [0]
cost = 0

result = []
def tspFinder(path, visited, cost):
    inf = float('inf')
    ans = inf

    if len(path) == 4 :
        res = cost + dist[path[-1]][0]
        dic = {res: path}
        result.append(res)
        if res == min(result) :
            print(dic.values())
        return res

    for city in range(N):
        if visited == 1<<city : continue
        elif visited & (1 << city) == 0 and dist[path[-1]][city] !=0 and dist[path[-1]][city] < 10 :
            cur = path[-1]
            visited = 1<<1
            path.append(city)
            temp_c = tspFinder(path, visited, cost + dist[cur][city])
            ans = min(ans, temp_c)
            path.pop()
            visited = 1>>1

    return ans

print(tspFinder(path, visited, cost))