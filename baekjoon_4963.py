import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         dfs(x-1, y + 1)
#         dfs(x-1, y - 1)
#         dfs(x+1, y + 1)
#         dfs(x+1, y - 1)
#         return True
#     return False
#

def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

while True:
    m, n = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, input().split()))

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
                dfs(i, j)

    print(count)

