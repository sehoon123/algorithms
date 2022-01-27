import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
graph = [[] for _ in range(20001)]
distance = [INF] * 20001

N,M,C = map(int,input().split())
for _ in range(M):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))

q = []
heapq.heappush(q, (C, 0))
distance[C] = 0
while q:
    node, cost = heapq.heappop(q)
    if distance[node] < cost:
        continue
    for next_node, next_cost in graph[node]:
        if distance[next_node] > distance[node] + next_cost:
            distance[next_node] = distance[node] + next_cost
            heapq.heappush(q, (next_node, distance[next_node]))

count = 0
max = -1
for i in distance:
    if i == INF or i == 0:
        continue
    else:
        if i > max:
            max = i
        count += 1

print(count, max)
