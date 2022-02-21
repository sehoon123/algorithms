import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))

if n == 1:
    print(0)
    exit(0)

dp = [0] * (n+1)
dp[1] = 0

for i in range(1, n+1):
    for j in range(1,arr[i]+1):
        if i + j > n:
            break
        if dp[i+j] == 0:
            if i != 1 and dp[i] == 0:
                print(-1)
                exit(0)
            dp[i+j] = dp[i] + 1
        else:
            dp[i+j] = min(dp[i]+1, dp[i+j])

if dp[-1] != 0:
    print(dp[-1])
else:
    print(-1)
