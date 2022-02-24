import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
orange = [0]
for _ in range(n):
    orange.append(int(input()))

dp[1][1] = k
for i in range(2, n + 1):
    for j in range(1, m + 1):