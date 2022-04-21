dp = [[0]*1001 for _ in range(1001)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1
mod = 10007

n, k = map(int, input().split())
for i in range(2, n+1):
    for j in range(k+1):
        # dp[i][j] = (dp[i-1][j]%mod + dp[i-1][j-1]%mod)%mod
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1])

# print(dp[n][k]%mod)
print(dp[n][k])