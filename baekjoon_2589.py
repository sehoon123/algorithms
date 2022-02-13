import sys
from collections import deque
input = sys.stdin.readline


l, w = map(int, input().split())
graph = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(l):
    graph.append(list(input().strip()))


def bfs(i, j):
    q = deque()
    q.append((i, j))
    now = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < w and graph[nx][ny] != 'W' and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                now = max(now, graph[nx][ny])
    return now


MAX = 0
for i in range(l):
    for j in range(w):
        if graph[i][j] != 'W':
            visit = [[0] * w for _ in range(l)]
            graph[i][j] = 0
            visit[i][j] = 1
            MAX = max(MAX, bfs(i, j))

print(MAX)