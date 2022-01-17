n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            left = 0
        else:
            left = graph[i-1][j-1]
        if j == i:
            right = 0
        else:
            right = graph[i-1][j]
        graph[i][j] += max(left,right)
print(max(graph[n-1]))
