import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

graph = []
visited = [[0]*m for _ in range(n)]
q = deque()
count = 0
max_size = 0


def bfs(x,y):
    global max_size
    temp = 0
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                temp += 1

    if temp == 0:
        temp = 1
    if temp > max_size:
        max_size = temp



for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j)
            count += 1

print(count)
print(max_size)



