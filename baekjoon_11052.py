import sys
input = sys.stdin.readline

n = int(input())
cards= list((map(int, input().split())))

dp = [0] * (n+1)
dp[1] = cards[0]

for i in range(2, n+1):
    dp[i] = cards[i-1]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i-j] + cards[j-1])

print(dp[-1])