from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,0,0,1]
dy = [0,1,-1,0]


def bfs(sx, sy):
    q = deque()
    q.append((sx,sy))
    man_visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == 0 or y == 0 or x == h-1 or y == w - 1:
            return man_visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if man_visited[nx][ny] == 0 and graph[nx][ny] == '.' and man_visited[x][y] + 1 < fire_visited[nx][ny]:
                    man_visited[nx][ny] = man_visited[x][y] + 1
                    q.append((nx,ny))
    return "IMPOSSIBLE"


def bfs_fire():
    while fireq:
        x, y = fireq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if fire_visited[nx][ny] == 1000000 and (graph[nx][ny] == '.' or graph[nx][ny] == 'J'):
                    fire_visited[nx][ny] = fire_visited[x][y] + 1
                    fireq.append((nx,ny))


h, w = map(int, input().split())
graph = []
sx, sy = 0, 0
fireq = deque()
fire_visited = [[1000000]*w for _ in range(h)]
man_visited = [[0]*w for _ in range(h)]
for i in range(h):
    graph.append(input().strip())
    for j in range(w):
        if graph[i][j] == 'J':
            sx, sy = i, j
        if graph[i][j] == 'F':
            fireq.append((i,j))
            fire_visited[i][j] = 1

bfs_fire()
print(bfs(sx, sy))