import sys
import copy
from collections import deque
input = sys.stdin.readline

graph = []
n, m = map(int, input().split())
ans = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def check(temp):
    global ans
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1

    ans = max(ans, cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0

def bfs():
    q = deque()
    temp = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))

    check(temp)

wall(0)
print(ans)


