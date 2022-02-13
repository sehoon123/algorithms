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


def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < w and temp[nx][ny] == 'L':
                temp[nx][ny] = 'W'
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
                cnt = max(cnt, distance[nx][ny])
    return cnt


MAX = 0
for i in range(l):
    for j in range(w):
        temp = copy.deepcopy(graph)
        if temp[i][j] == 'L':
            temp[i][j] = 'W'
            distance = [[0] * w for _ in range(l)]
            MAX = max(MAX, bfs(i, j))

print(MAX)
