import sys
input = sys.stdin.readline
n = int(input())

brick = [(0, 0, 0, 0)]
for i in range(1, n + 1):
    a, b, c = map(int, sys.stdin.readline().split())
    brick.append((i, a, b, c))

brick.sort(key=lambda x: x[3])

dp = [0] * (n + 1)

for now in range(1, n + 1):
    for prev in range(0, now):
        if brick[now][1] > brick[prev][1]:
            dp[now] = max(dp[now], dp[prev] + brick[now][2])

max_height = max(dp)
idx = dp.index(max_height)
result = []

while idx > 0:
    if max_height == dp[idx]:
        result.append(brick[idx][0])
        max_height -= brick[idx][2]
    idx -= 1
print(len(result))
for i in reversed(result):
    print(i)