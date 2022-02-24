import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = [0] * (n+1)
dp[1] = k
orange = [0]
for _ in range(n):
    orange.append(int(input()))

for i in range(2, n+1):
    dp[i] = dp[i-1] + k

for i in range(0, n):
    min_orange = orange[i+1]
    max_orange = orange[i+1]
    for j in range(1,m+1):
        if i + j > n:
            break
        min_orange = min(min_orange, orange[i+j])
        max_orange = max(max_orange, orange[i+j])
        dp[i + j] = min(dp[i + j], dp[i] + k + j * (max_orange - min_orange))

print(dp[-1])