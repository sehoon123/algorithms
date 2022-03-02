import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int,input().split())
cows = [[0]*2 for _ in range(n+1)]


for i in range(1, n+1):
    a, b = map(int,input().split())
    cows[i][0] = a
    cows[i][1] = b

graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


visited = [0]*(n+1)
group = []

def dfs(x):
    visited[x] = 1
    temp.append(x)
    for node in graph[x]:
        if visited[node] == 0:
            dfs(node)

for i in range(1, n+1):
    if visited[i] == 0:
        temp = []
        dfs(i)
        group.append(temp)

fence = 1e9
for i in range(len(group)):
    left,right,up,down = 1e9,0,0,1e9
    for v in group[i]:
        if cows[v][0] < left:
            left = cows[v][0]
        if cows[v][0] > right:
            right = cows[v][0]
        if cows[v][1] < down:
            down = cows[v][1]
        if cows[v][1] > up:
            up = cows[v][1]
    if fence > 2*((right-left)+(up-down)):
        fence = 2*((right-left)+(up-down))

print(fence)

