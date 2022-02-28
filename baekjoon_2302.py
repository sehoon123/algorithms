import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]
dp = [0]* (n+1)
dp[1] = 1


for i in range(2, n+1):
    if i in vip:
        dp[i] = dp[i-1]
    elif i == 2:
        if 1 in vip:
            dp[2] = 1
        else:
            dp[i] = 2
    elif i-1 in vip:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
