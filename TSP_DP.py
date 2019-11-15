# 재귀 없이
from pprint import pprint

INF = 10000
dist = [[0, 2, 9, INF],
        [1, 0, 6, 4],
        [INF, 7, 0, 8],
        [6, 3, INF, 0]]
N = len(dist)

path = [0]
cost = 0
VISITED_ALL = (1 << N)-1 # 1111
visited = 1 << 4 #1000

result = []
def tsp_dp (path, visited, cost) :
    inf = float('inf')
    ans = inf
    memo = [[0 for x in range(N-1)] for x in range(N)]


    def subpath (start, end) :
        if dist[start][end] != 0 and dist[start][end] < inf :
            return dist[start][end]
        elif dist[start][end] == inf :
            for i in range(N) :
                ans = min(subpath(start,i) + subpath(i,end))
                return ans
    pprint(path)

# print(tsp_dp(path, visited, cost))

tsp_dp(path, visited, cost)