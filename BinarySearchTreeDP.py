INT_MAX = 2147483647

def optimalSearchTree(keys, freq, n):
    cost = [[0 for x in range(n)]
            for y in range(n)] # 초기화

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 2): # i는 열 j는 행
            j = i + L - 1
            if i >= n or j >= n:
                break
            cost[i][j] = INT_MAX

            for r in range(i, j + 1):
                c = 0
                if (r > i):
                    c += cost[i][r - 1]
                if (r < j):
                    c += cost[r + 1][j]
                c += sum(freq, i, j)
                if (c < cost[i][j]):
                    cost[i][j] = c
    return cost[0][n - 1]

def sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


if __name__ == '__main__':
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    n = len(keys)
    print("Cost of Optimal Binary Search Tree is",
          optimalSearchTree(keys, freq, n))