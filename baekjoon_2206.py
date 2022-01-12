from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

crash = [[False] * m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    while queue:
        for i in crash:
            print(i)

        print()
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if nx == n-1 and ny == m-1:
                graph[nx][ny] = graph[a][b] + 1
                break
            if graph[nx][ny] == 1 and not crash[a][b]:
                crash[nx][ny] = True
                graph[nx][ny] = graph[a][b] + 1
                queue.append([nx,ny])

            if graph[nx][ny] == 0:
                crash[nx][ny] = crash[a][b]
                graph[nx][ny] = graph[a][b] + 1
                queue.append([nx,ny])

bfs(0,0)


if m != 1 and n != 1:
    if graph[n-1][m-1] == 0:
        print(-1)
        exit(0)

print(graph[n-1][m-1]+1)
