from pprint import pprint

graph = [[0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 0],
         [1, 1, 0, 1, 1, 0],
         [0, 1, 1, 0, 1, 1],
         [0, 1, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 0]]
print("Structure of Node")
pprint(graph)

for i in range(len(graph)) :
    list = graph[i]
    ans = []
    for j in range(len(graph)) :
        if list[j] == 1 :
            where = []
            where.append(j)
    print(i+1, "번째 노드의 인접 노드 :", where)
    del where
