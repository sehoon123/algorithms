import math
n = int(input())

dp = [0] * 50001
dp[1] = 1

for i in range(2, n+1):
    MIN = 5
    for j in range(1, int(math.sqrt(i))+1):
        tmp = i - j**2
        MIN = min(MIN, dp[tmp])
    dp[i] = MIN + 1

print(dp[n])