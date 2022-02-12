import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def dfs(x,y, target):
    if temp[x][y] <= target:
        return
    temp[x][y] = target
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            dfs(nx, ny, target)

MAX = 0
for k in range(100):
    temp = graph
    num = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j] > k:
                dfs(i, j, k)
                num += 1
    MAX = max(MAX, num)

print(MAX)


