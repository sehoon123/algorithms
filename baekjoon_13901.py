import sys
input = sys.stdin.readline
r, c = map(int, input().split())
k = int(input())
visited = [[0] * c for _ in range(r)]

for _ in range(k):
    x, y = map(int, input().split())
    visited[x][y] = 1

sx, sy = map(int, input().split())
visited[sx][sy] = 1
direction = list(map(int, input().split()))
for i in range(4):
    direction[i] -= 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
pos = 0
dirSet = set()
ans = []

while 1:
    dirSet.add(direction[pos])
    nx = sx + dx[direction[pos]]
    ny = sy + dy[direction[pos]]
    if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[nx][ny] == 1:
        pos += 1
        pos %= 4
        if pos in dirSet:
            ans.append(sx)
            ans.append(sy)
            break
        else:
            continue
    else:
        dirSet = set()
        visited[nx][ny] = 1
        sx = nx
        sy = ny

print(ans[0], ans[1])

