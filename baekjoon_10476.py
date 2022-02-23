import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0,0]]
for _ in range(n):
    graph.append(list(map(int, input().split())))
aaa, bbb = map(int, input().split())
if k == 0:
    total = 0
    for i in range(1, n+1):
        total += sum(graph[i])

    print(total)
    sys.exit()

dp = [[[0]*3 for _ in range(k+1)] for _ in range(n+1)]
# 모두 다 닫지 않은 경우
dp[1][0][0] = graph[1][0] + graph[1][1]
# 왼쪽방을 닫은경우
dp[1][1][1] = graph[1][1]
# 오른쪽방을 닫은경우
dp[1][1][2] = graph[1][0]

for i in range(2, n+1):
    for j in range(k+1):
        if j > i:
            break
        if j >= 1:
            dp[i][j][1] = max(dp[i-1][j-1][0], dp[i-1][j-1][1]) + graph[i][1]
            dp[i][j][2] = max(dp[i-1][j-1][0], dp[i-1][j-1][2]) + graph[i][0]
        if i != j:
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1], dp[i-1][j][2]) + graph[i][0] + graph[i][1]

print(max(dp[n][k][0], dp[n][k][1], dp[n][k][2]))