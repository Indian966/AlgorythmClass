INF = 10000
dist = [[0, 2, 9, INF],
        [1, 0, 6, 4],
        [INF, 7, 0, 8],
        [6, 3, INF, 0]]

# visited = [1, 0, 0, 0]
path = [0]
cost = 0

def tsp(D):
    N = len(D)
    inf = float('inf')
    ans = inf
    VISITED_ALL = (1 << N) - 1

    def find_path(start, last,path, visited, tmp_dist):
        nonlocal ans
        if visited == VISITED_ALL:
            return_home_dist = D[last][start] or inf
            ans = min(ans, tmp_dist + return_home_dist)
            path.pop()
            # if ans > tmp_dist + return_home_dist :
            #     ans = tmp_dist + return_home_dist
            return

        for city in range(N):
            if visited & (1 << city) == 0 and D[last][city] != 0:
                path.append(city)
                find_path(start, city,path, visited | (1 << city), tmp_dist + D[last][city])

    for c in range(N):
        find_path(c, c,path, 1 << c, 0)
    return ans, path

print(tsp(dist))
