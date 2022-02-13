import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[x][y] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global count
    if graph[x][y] == 1:
        return
    count += 1
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx, ny)


result = []
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            result.append(count)
            count = 0

print(len(result))
for v in sorted(result):
    print(v, end=" ")
