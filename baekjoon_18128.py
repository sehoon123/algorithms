from collections import deque
import sys
input = sys.stdin.readline

n, w = map(int, input().split())
graph = []
pond = []
water = [[0] * n for _ in range(n)]
movement = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]
for _ in range(w):
    pond.append(list(map(int, input().split())))

for i in range(n):
    graph.append(input().strip())

q = deque()
for v in pond:
    q.append((v[0] - 1, v[1] - 1))
    water[v[0] - 1][v[1] - 1] = 1

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if water[nx][ny] == 0:

                    water[nx][ny] = water[x][y] + 1
                    q.append([nx, ny])

def move():
    location = deque()
    location.append([0, 0])
    movement[0][0] = 1
    while location:
        x, y = location.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == '1' and movement[nx][ny] == 0:
                    movement[nx][ny] = movement[x][y] + 1
                    location.append([nx, ny])

def check(mid):
    if 




def bianry(left, right):
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
            result = mid
        else:
            left = mid + 1
    return result




bfs()
print(water)
move()
print(movement)