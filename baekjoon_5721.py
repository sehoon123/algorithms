import sys
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    dp = [0] * m
    if m == 0 and n == 0:
        break
    graph = []
    for _ in range(m):
        graph.append(list(map(int, input().split())))

    for i in range(m):
        now = [0] * n
        now[0] = graph[i][0]
        if n != 1:
            now[1] = max(graph[i][0], graph[i][1])
        for j in range(2,n):
            now[j] = max(now[j-1], now[j-2] + graph[i][j])
        if i == 0:
            dp[0] = now[n-1]
        elif i == 1:
            dp[1] = max(dp[0], now[n-1])
        else:
            dp[i] = max(dp[i-1], dp[i-2] + now[n-1])

    print(dp[m-1])


