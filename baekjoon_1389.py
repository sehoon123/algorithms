import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
sys.setrecursionlimit(n*m)
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in adj[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)

idx = 0
kevin = int(1e9)
for i in range(1, n+1):
    bfs(i)
    if kevin > sum(visited) - visited[i]:
        idx = i
        kevin = sum(visited) - visited[i]
    visited = [0] * (n+1) 

print(idx)
