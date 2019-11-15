INF = 10000
dist = [[0, 2, 9, INF],
        [1, 0, 6, 4],
        [INF, 7, 0, 8],
        [6, 3, INF, 0]]
N = len(dist)
path = [0]
cost = 0
VISITED_ALL = (1 << N)-1 # 1111
visited = 1 << 0 #1

def tsp_dp (path, visited, cost) :
    inf = float('inf')
    memo = [[None] * (1 << N) for _ in range(N)]

    def subpath(end, visited) :
        if visited == VISITED_ALL :
            return dist[end][0] or inf
        if memo[end][visited] is not None:
            return memo[end][visited]

        temp_c = inf
        for city in range(N):
            if visited & 1 << city: continue
            if visited & (1 << city) == 0 and dist[end][city] !=0 :
                temp_c = min(temp_c, subpath(city, visited | (1 << city)) + dist[end][city])
        memo[end][city] = temp_c
        return temp_c

    return subpath(0, visited)

print(tsp_dp(path, visited, cost))
