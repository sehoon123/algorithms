import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)


def bfs(start, end):
    q = deque([start])
    visited[start] = 1
    while q:
        cur = q.popleft()
        if cur == end:
            return
        for next in adj[cur]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = visited[cur] + 1


bfs(a, b)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b]-1)
