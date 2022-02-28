MOD = 1000000007
dp = [[0] * 3001 for _ in range(3001)]
dp[0][0] = 1

s = int(input())
word = input().rstrip()

for i in range(1, len(word)+1):
    sum = 0
    for j in range(s+1):
        sum = (sum + dp[i-1][j]) % MOD
        if j > 25:
            sum = (sum - dp[i-1][j-26] + MOD) % MOD
        dp[i][j] = sum

print(dp[len(word)][s])