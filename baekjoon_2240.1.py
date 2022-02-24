t, w = map(int,input().split())

arr = [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w+1)] for _ in range(t)]

for i in range(t):
    for j in range(w+1):
        if j == 0:
            if arr[i] == 1:
                dp[i][j] = dp[i-1][j]+1
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if arr[i] == 1 and j % 2 == 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            elif arr[i] == 2 and j % 2 == 1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

# print(max(dp[-1]))
print(dp[t-1][w])
