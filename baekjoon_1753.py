import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

distance = [INF] * 20001
visited = [False] * 20001
graph = [[] for _ in range(20001)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def getSmallest():
    min = INF
    min_index = 0
    for i in range(1, v + 1):
        if not visited[i] and distance[i] < min:
            min = distance[i]
            min_index = i

    return min_index


dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
