import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = []
p = [0] * (n+1)
dp = [0]*(n+1)
for _ in range(k):
    day, pasta = map(int, input().split())
    temp.append([day, pasta])
    p[day] = pasta


dp[0] = 1
for i in range(1,n+1):
    if p[i] != 0:
        dp[i] = dp[i-1]
    if p[i-1] == p[i-2]:
        dp[i] = dp[i-1]*2
    else:
        dp[i] = dp[i-1]*3
    
print(dp)

