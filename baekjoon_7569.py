from collections import deque
m, n, h = map(int, input().split())
graph = []
tomato = deque()

for k in range(h):
    graph.append([])
    for i in range(n):
        line = list(map(int,input().split()))
        graph[k].append(line)
        for j in range(len(line)):
            if line[j] == 1:
                tomato.append([k, i, j])

# print(tomato)

dx = [-1,0,0,0,0,1]
dy = [0,1,-1,0,0,0]
dz = [0,0,0,1,-1,0]

def bfs():
    while tomato:
        c, a, b = tomato.popleft()
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[c][a][b] + 1
                tomato.append([nz, nx, ny])

bfs()
result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
        result = max(result, max(graph[i][j]))

print(result-1)