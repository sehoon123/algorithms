from collections import deque

def bfs():
    queue = deque()
    queue.append([s_x,s_y])
    while queue:
        x, y = queue.popleft()

        if x == d_x and y == d_y:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])

T = int(input())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

for i in range(T):
    n = int(input())
    s_x, s_y = map(int, input().split())
    d_x, d_y = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    bfs()
    print(graph[d_x][d_y])

