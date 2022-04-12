import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))


distance = [INF] * (n+1)
q = [(0, x)]

# COMEBACK
distance[x] = 0

while q:
    cost, now = heapq.heappop(q)

    if distance[now] < cost:
        continue
    
    for v in graph[now]:
        if distance[v[1]] > cost + v[0]:
            distance[v[1]] = cost + v[0]
            heapq.heappush(q, (cost + v[0], v[1]))

# print(distance)


MAX = 0
for i in range(1, n+1):
    temp = [INF] * (n+1)
    q = [(0, i)]
    temp[i] = 0
    while q:
        cost, now = heapq.heappop(q)

        if temp[now] < cost:
            continue

        for v in graph[now]:
            if temp[v[1]] > cost + v[0]:
                temp[v[1]] = cost + v[0]
                heapq.heappush(q, (cost + v[0], v[1]))

    if distance[i] + temp[x] > MAX:
        MAX = distance[i] + temp[x]



print(MAX)
