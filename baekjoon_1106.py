import sys
input = sys.stdin.readline

c, n = map(int, input().split())
price = []
for _ in range(n):
    price.append(list(map(int,input().split())))

dp = [0]*(100001)
for i in range(n):
    for j in range(1, 100001):
        if price[i][0] * j > 1000:
            break
        if dp[price[i][0]*j] == 0:
            dp[j*price[i][0]] = j * price[i][1]
        else:
            dp[j*price[i][0]]=max(j*price[i][1], dp[j*price[i][0]])

for i in range(1,100001):
    for j in range(n):
        if i-price[j][0] < 1:
            continue
        dp[i] = max(dp[i-price[j][0]]+dp[price[j][0]], dp[i])
    if dp[i] >= c:
        print(i)
        break

