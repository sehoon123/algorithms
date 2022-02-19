from collections import deque
import copy
import sys


input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = []


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit = [[0] * m for i in range(n)]
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and temp[nx][ny] != 0:
                temp[nx][ny] = 0
                visit[nx][ny] = 1
                q.append([nx, ny])


def check(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and t[nx][ny] == 0:
            cnt += 1
    return cnt


def checkz():
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                return False
    return True


for i in range(n):
    graph.append(list(map(int, input().split())))
result = 1


while True:
    if checkz():
        print(0)
        break
    t = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if t[i][j] != 0:
                temp = graph[i][j] - check(i, j)
                graph[i][j] = temp if temp >= 0 else 0
    temp = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] != 0:
                temp[i][j] = 0
                bfs(i, j)
                cnt += 1
    if cnt > 1:
        print(result)
        break
    result += 1