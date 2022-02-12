import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input().strip()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sheep = 0
wolves = 0


def dfs(x, y):
    global sheep, wolves
    if graph[x][y] == '#':
        return
    if graph[x][y] == 'v':
        wolves += 1
    if graph[x][y] == 'o':
        sheep += 1
    graph[x][y] = '#'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            dfs(nx, ny)

score = [0, 0]
for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':
            dfs(i, j)
            if sheep > wolves:
                score[0] += sheep
            else:
                score[1] += wolves
            sheep = 0
            wolves = 0

print(score[0], score[1])