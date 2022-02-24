import sys
input = sys.stdin.readline

first = input().strip()
second = input().strip()

dp = [[0]*(len(first)+1) for _ in range(len(second)+1)]

for i in range(1,len(second)+1):
    for j in range(1,len(first)+1):
        if second[i-1] == first[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])


x = len(second)
y = len(first)
result = []

while dp[x][y]:
    if dp[x][y] == dp[x-1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    elif dp[x][y] == dp[x-1][y-1] + 1 :
        result.append(first[y-1])
        x -=1
        y -= 1

ans = result[::-1]
print(''.join(ans))

