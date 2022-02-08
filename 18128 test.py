from collections import deque
import sys
input = sys.stdin.readline

n, w = map(int, input().split())
graph = []
pond = []
#물이 차오르는 날자
water = [[-1] * n for _ in range(n)]

max_water = -1

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]
for _ in range(w):
    pond.append(list(map(int, input().split())))

for i in range(n):
    graph.append(input().strip())

q = deque()
for v in pond:
    q.append((v[0] - 1, v[1] - 1))
    water[v[0] - 1][v[1] - 1] = 0

def WaterDepth():
    global max_water
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if water[nx][ny] == -1:
                    water[nx][ny] = water[x][y] + 1
                    q.append([nx, ny])
    for i in range(n):
        for j in range(n):
            if water[i][j] > max_water:
                max_water = water[i][j]

def check(mid):
    # 위치를 방문한 여부
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    location = deque()
    location.append([0, 0])

    while location:
        x, y = location.popleft()
        if (x == n - 2 and y == n - 1) or (x == n - 1 and y == n - 2) or (x == n-2 and y == n-2):
            return True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == '1' and water[nx][ny] <= mid:
                    visited[nx][ny] = 1
                    location.append([nx, ny])
    return False




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

WaterDepth()
left, right = 0, max_water
result = bianry(left, right)
print(result)
