import sys
input = sys.stdin.readline


while True:
    n, m = map(float, input().split())
    n = int(n)
    if n == 0 and m == 0.00:
        break
    m = int(m * 100)
    dp = [0] * (m+1)
    for i in range(n):
        c, p = map(float, input().split())
        p = int(p * 100)
        for i in range(p, m+1):
            dp[i] = max(dp[i], dp[i-p] + c)

    print(int(dp[-1]))

