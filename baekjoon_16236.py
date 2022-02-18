from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어의 위치
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        #상어를 찾으면 종료
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx, sy = i, j
            break

size = 2
move_num = 0
eat = 0
while True:
    q = deque()
    #상어의 위치와 크기를 큐에 저장
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        x, y, count = q.popleft()

        #물고기를 먹은후 먹은 물고기보다 더 가까운 먹을수 있는 물고기가 없으면 종료
        if count > flag:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] <= size:
                    #물고기를 먹을수 있을때
                    if graph[nx][ny] != 0 and graph[nx][ny] < size:
                        #물고기를 먹음
                        fish.append((nx, ny, count + 1))
                        #물고기를 먹는데 걸린 기간
                        flag = count
                    visited[nx][ny] = True
                    q.append((nx, ny, count + 1))

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        eat += 1
        graph[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        #물고기를 먹은 위치에서 다시시작
        sx, sy = x, y
    else:
        break

print(move_num)