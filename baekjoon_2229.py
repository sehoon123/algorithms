import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n+1):
    MAX = -1
    MIN = 1e9
    for j in range(i, 0, -1):
        MAX = max(MAX, arr[j])
        MIN = min(MIN, arr[j])
        dp[i] = max(dp[i], MAX-MIN + dp[j-1])

print(dp)
print(dp[-1])



