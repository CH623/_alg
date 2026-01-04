import heapq

def dijkstra(graph, start):
    """
    graph: dict
        graph[u] = [(v, weight), ...]
    start: 起點
    """

    # 初始化距離
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    # 優先佇列 (距離, 節點)
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # 如果這個距離不是最新的，就跳過
        if current_dist > dist[u]:
            continue

        # 檢查鄰居
        for v, weight in graph[u]:
            new_dist = dist[u] + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

result = dijkstra(graph, 'A')
print(result)
