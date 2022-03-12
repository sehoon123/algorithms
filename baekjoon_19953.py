import sys
input = sys.stdin.readline

v, m, t = map(int,input().split())

sx, sy = 0, v
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(1,t):
    sx, sy = sx+((v*m)%10)*dx[i%4], sy+((v*m)%10)*dy[i%4]

print(sx,sy)

