graph = {
        '1' : ['2', '3', '4'],
        '2' : ['4'],
        '3' : ['4'],
        '4' : ['1', '2', '3']
    }

def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit

print(dfs(graph,'1'))
print(bfs(graph,'1'))