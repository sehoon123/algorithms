mod = 998244353
n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(1,10):
        if j == 9:
            dp[i][j] = dp[i-1][j-1]%mod + dp[i-1][j]%mod
        else:
            dp[i][j] = dp[i-1][j-1]%mod + dp[i-1][j]%mod + dp[i-1][j+1]%mod

print(sum(dp[n])%mod)
