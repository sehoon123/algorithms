import sys
import itertools
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
pan = list(map(int, input().split()))
can = list(itertools.combinations(pan, 2))

dp = [INF] *10001

for v in can:
    pan.append(sum(v))

pan = set(pan)
for v in pan:
    if v < 10001:
        dp[v] = 1


for i in range(1, n+1):
    for j in pan:
        if i - j < 0:
            continue
        dp[i] = min(dp[i], dp[i-j] +1)


if dp[n] == INF:
    print(-1)
else:
    print(dp[n])