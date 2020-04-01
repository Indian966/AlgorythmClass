import heapq

graph_dict = {
    "v1": {"v2": 7, "v3": 4, "v4": 6, "v5": 1},
    "v2": {},
    "v3": {"v2": 2, "v4": 5, },
    "v4": {"v2": 3},
    "v5": {"v4": 1,},
}

def Dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    res = 0
    list = ['v1', 'v2', 'v3', 'v4', 'v5']

    for i in list:
        res+=distances.get(i)

    print("The shortest path is :", res)

    return distances

print(Dijkstra(graph_dict, 'v1'))