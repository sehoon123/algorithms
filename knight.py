box = [[0]*8 for _ in range(8)]

raw = input()

x = ord(raw[0]) - ord('a')
y = int(raw[1]) -1

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        continue
    count += 1

print(count)