import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
r = []
g = []
b = []
dp_r = [[0]*3 for _ in range(n+1)]
dp_g = [[0]*3 for _ in range(n+1)]
dp_b = [[0]*3 for _ in range(n+1)]

for _ in range(n):
    x, y, z = map(int, input().split())
    r.append(x)
    g.append(y)
    b.append(z)

dp_r[1][0] = r[0]
dp_r[1][1] = INF
dp_r[1][2] = INF

dp_g[1][0] = INF
dp_g[1][1] = g[0]
dp_g[1][2] = INF

dp_b[1][0] = INF
dp_b[1][1] = INF
dp_b[1][2] = b[0]

# dp_r[1][0] = r[0]
# dp_r[1][1] = g[0]
# dp_r[1][2] = b[0]


for i in range(2, n+1):
    for j in range(3):
        if j == 0:
            dp_r[i][j] = min(dp_r[i-1][1], dp_r[i-1][2]) + r[i-1]
            dp_g[i][j] = min(dp_g[i-1][1], dp_g[i-1][2]) + r[i-1]
            dp_b[i][j] = min(dp_b[i-1][1], dp_b[i-1][2]) + r[i-1]
        elif j == 1:
            dp_r[i][j] = min(dp_r[i-1][2], dp_r[i-1][0]) + g[i-1]
            dp_g[i][j] = min(dp_g[i-1][2], dp_g[i-1][0]) + g[i-1]
            dp_b[i][j] = min(dp_b[i-1][2], dp_b[i-1][0]) + g[i-1]
        else:
            dp_r[i][j] = min(dp_r[i-1][1], dp_r[i-1][0]) + b[i-1]
            dp_g[i][j] = min(dp_g[i-1][1], dp_g[i-1][0]) + b[i-1]
            dp_b[i][j] = min(dp_b[i-1][1], dp_b[i-1][0]) + b[i-1]




print(min(min(dp_r[n][1], dp_r[n][2]), min(dp_g[n][0],dp_g[n][2]), min(dp_b[n][0], dp_b[n][1])))

