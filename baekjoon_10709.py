import sys
input = sys.stdin.readline

n, m = map(int,input().split())

plan = [[-1]*m for _ in range(n)]

graph = []
for i in range(n):
    graph.append(input().strip())
    for j in range(len(graph[i])):
        if graph[i][j] == 'c':
            plan[i][j] = 0

for i in range(n):
    for j in range(1,m):
        if plan[i][j-1] != -1:
            if plan[i][j] == 0:
                continue
            plan[i][j] = plan[i][j-1] + 1

for v in plan:
    print(*v)