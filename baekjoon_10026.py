import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

n = int(input())
graph = []
for _ in range(n):
    graph.append(input().strip())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[False]*n for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == graph[x][y]:
                dfs(nx,ny)


def dfs_err(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False:
                if graph[x][y] == 'R' or graph[x][y] == 'G':
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        dfs_err(nx,ny)
                elif graph[x][y] == 'B' and graph[nx][ny] == 'B':
                    dfs_err(nx,ny)


count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            count += 1

print(count)


visited = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs_err(i,j)
            count += 1

print(count)
