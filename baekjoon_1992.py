import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(input().strip())

# print(graph)

def f(sx, sy, ex, ey):
    flag = True
    for i in range(sx,ex):
        for j in range(sy,ey):
            if graph[i][j] != graph[sx][sy]:
                flag = False
                f(sx, sy, sx+(ex-sx)/2, sy+(ey-sy)/2)
                f(sx, sy+(ey-sy)/2, sx + (ey-sy)/2, ey)
                f(sx+(ey-sy)/2, sy, ex, sy+(ey-sy)/2)
                f(sx+(ey-sy)/2, sy+(ey-sy)/2, ex, ey)
                return

    if flag:
        if graph[sx][sy] == 0:
            print(0,end="")
        else:
            print(1,end="")

f(0,0,n,n)
