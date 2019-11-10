INF = 1000000000
m = [[0, 1, INF, 1, 5],
     [9, 0, 3, 2, INF],
     [INF, INF, 0, 4, INF],
     [INF, INF, 2, 0, 3],
     [3, INF, INF, INF, 0]]

def floyd_warshall(vertex, adjacency_matrix):
    path = [[0] * vertex for i in range(vertex)]

    for k in range(0, vertex):
        for i in range(0, vertex):
            for j in range(0, vertex):
                sum_ik_kj = adjacency_matrix[i][k] + adjacency_matrix[k][j]
                if adjacency_matrix[i][j] > sum_ik_kj:
                    adjacency_matrix[i][j] = sum_ik_kj
                    path[i][j] = k+1
    print("가중치")
    print(" ", end='')
    for i in range(0, vertex):
        print("\t{:d}".format(i + 1), end='')
    print();
    for i in range(0, vertex):
        print("{:d}".format(i + 1), end='')

        for j in range(0, vertex):
            print("\t{:d}".format(adjacency_matrix[i][j]), end='')
        print();

    print("---------------------")

    print("거쳐간 경로")
    print(" ", end='')
    for i in range(0, vertex):
        print("\t{:d}".format(i + 1), end='')
    print();
    for i in range(0, vertex):
        print("{:d}".format(i + 1), end='')

        for j in range(0, vertex):
            print("\t{:d}".format(path[i][j]), end='')
        print();

floyd_warshall(5, m);

#   i라는 경로에서 j라는 경로로 갈때 n번 노드를 거쳐가는 최소를 계산
#   지나가면서 어떤 path를 거쳤는지 확인
#   재귀를 이용, 트리를 만들어서 왼쪽에서 재귀, 오른쪽에서 재귀
#   최단경로, 거쳐간 노드 출력
