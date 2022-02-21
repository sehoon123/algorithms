import sys
input = sys.stdin.readline

n = int(input())
schedule = []
dp = [0] * 21
for i in range(n):
    schedule.append(list(map(int, input().split())))

for i in range(n-1, -1, -1):
    if i + schedule[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i + 1])

print(dp[0])
