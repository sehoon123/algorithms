import copy
import sys
from collections import deque
input = sys.stdin.readline


l, w = map(int, input().split())
graph = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(l):
    graph.append(list(input().strip()))


def bfs():
    global cnt
    while q:
        x, y = q.popleft()
        temp[x][y] = 'W'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < w and temp[nx][ny] == 'L':
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
                cnt = max(cnt, distance[nx][ny])


MAX = 0
cnt = 0
for i in range(l):
    for j in range(w):
        temp = copy.deepcopy(graph)
        if temp[i][j] == 'L':
            distance = [[0] * w for _ in range(l)]
            q = deque()
            q.append((i, j))
            bfs()
            MAX = max(MAX, cnt)
            cnt = 0

print(MAX)