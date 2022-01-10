n, m = map(int, input().split())
# 동, 남, 서, 북
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# 서, 남, 동, 북
dx = [0,1,0,-1]
dy = [-1,0,1,0]

x, y, d = map(int, input().split())

box = []
for i in range(n):
    box.append(list(map(int,input().split())))

box[x][y] = 1
count = 1
while 1:
    if box[x+1][y] == 1 and box[x-1][y] == 1 and box[x][y-1] == 1 and box[x][y+1] == 1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if box[nx][ny] == 0:
            count += 1
            box[nx][ny] = 1
            x = nx
            y = ny
            break

print(count)
