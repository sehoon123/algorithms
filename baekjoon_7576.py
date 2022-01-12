from collections import deque

m, n = map(int, input().split())
graph = []
tomato = deque()

for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)
    for j in range(len(a)):
        if a[j] == 1:
            tomato.append((i, j))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    while tomato:
        a, b = tomato.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                tomato.append((nx,ny))
                graph[nx][ny] = graph[a][b] + 1


bfs()
ans = 0

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans-1)



