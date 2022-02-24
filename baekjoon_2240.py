import sys
input = sys.stdin.readline

t, w = map(int, input().split())
arr = [0] + [int(input()) for _ in range(t)]
dp = [[0] * (t+1) for _ in range(w + 1)]


for i in range(w+1):
    for j in range(1, t+1):
        if i == 0:
            if arr[j] == 1:
                dp[0][j] = dp[0][j-1] + 1
            else:
                dp[0][j] = dp[0][j-1]
        else:
            if dp[i-1][j-1] != dp[i-1][j]:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i][j-1]+1, dp[i-1][j])


# print(dp[w][t])
MAX = -1
for i in range(w+1):
    if dp[i][t] > MAX:
        MAX = dp[i][t]

print(MAX)

