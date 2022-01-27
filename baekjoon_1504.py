import sys
import heapq

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF] * (N + 1)
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            if next_cost + cost < dist[next_node]:
                dist[next_node] = next_cost + cost
                heapq.heappush(q, (dist[next_node], next_node))

    return dist[end]





input = sys.stdin.readline
N, E = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

result = min(dijkstra(1,v1)+dijkstra(v1,v2) + dijkstra(v2,N), dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N))

if result >= INF:
    print(-1)
else:
    print(result)