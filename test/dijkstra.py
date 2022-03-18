import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
start = int(input())
distance = [INF] * (v+1)
distance[start] = 0

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((c,b))


def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            if distance[i[1]] > dist + i[0]:
                distance[i[1]] = dist + i[0]
                heapq.heappush(q,(dist+i[0], i[1]))


dijkstra(start)

print(distance)
