import copy
import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, target):
    if temp[x][y] <= target:
        return
    temp[x][y] = target
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            dfs(nx, ny, target)

max_num = 0
for k in range(100):
    num = 0
    temp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if temp[i][j] > k:
                num += 1
                dfs(i, j, k)
    if num == 0:
        break

    max_num = max(max_num, num)

print(max_num)
