import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
visited = [[0] * n for _ in range(m)]
for i in range(m):
    a.append(input().strip())


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
white = []
blue = []

count = 0
count_blue = 0
count_white = 0

def dfs(x, y):
    global count_blue
    global count_white

    if visited[x][y] == 1:
        return

    if a[x][y] == 'B':
        count_blue += 1
    else:
        count_white += 1

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if a[nx][ny] == a[x][y] and visited[nx][ny] == 0:
            dfs(nx, ny)



for i in range(m):
    for j in range(n):
        result = dfs(i, j)
        if count_white > 0:
            white.append(count_white)
        elif count_blue > 0:
            blue.append(count_blue)
        count_blue = 0
        count_white = 0


total_w = 0
total_b = 0
for i in white:
    total_w += i**2
for i in blue:
    total_b += i**2

print(total_w, total_b)