import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m,x,y = map(int, input().split())
dist = [INF] * (n)
dist[y] = 0
graph = [[] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

q = [(0, y)]
while q:
    cost, node = heapq.heappop(q)

    if dist[node] < cost:
        continue

    for v in graph[node]:
        if dist[v[1]] > cost + v[0]:
            dist[v[1]] = cost + v[0]
            heapq.heappush(q, (cost + v[0], v[1]))

dist.sort()
count = 1
temp = 0
if dist[-1] * 2 > x:
    print(-1)
    exit(0)
for v in dist:
    if temp < x:
        temp += 2*v
        if temp > x:
            count += 1
            temp = 2*v
print(count)


