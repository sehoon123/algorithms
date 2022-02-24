import sys
input = sys.stdin.readline

n, t = map(int, input().split())
dp = [[0] * (t + 1) for _ in range(n + 1)]
time = []
score = []
for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    score.append(b)

for i in range(1, n+1):
    for j in range(1, t + 1):
        if j < time[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i-1]] + score[i-1])
print(dp[n][t])