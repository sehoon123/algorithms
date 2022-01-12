T = int(input())
for i in range(T):
    n,m,k = map(int,input().split())

    graph = [[0]*m for i in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1


    for i in range(n):
        print(graph[i])

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if graph[x][y] == 0:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            # print(dfs(i,j))
            if graph[i][j] == 1 and dfs(i,j):
                result += 1

    print(result)



