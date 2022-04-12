from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = []
q = []
blank = 0
INF = int(1e9)
result = INF

for i in range(n):
    que = list(map(int, input().split()))
    graph.append(que)
    for j in range(n):
        if que[j] == 2:
            q.append([i, j])
        if que[j] != 1:
            blank += 1
virus_candidates = list(combinations(q, m))


def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] != 1:
                visited[nx][ny] = 1
                que.append([nx, ny])
                move[nx][ny] = move[x][y] + 1


for i in virus_candidates:
    move = [[-1] * n for i in range(n)]
    visited = [[0] * n for i in range(n)]
    que = deque()
    for x, y in i:
        visited[x][y] = 1
        move[x][y] = 0
        que.append([x, y])
    bfs()
    cnt = 0
    for j in visited: cnt += j.count(1)
    if blank == cnt:
        max_n = 0
        for j in range(n):
            for k in range(n):
                if graph[j][k] != 1 and [j, k] not in q:
                    max_n = max(max_n, move[j][k])
        result = min(result, max_n)


print(result if result != INF else -1)