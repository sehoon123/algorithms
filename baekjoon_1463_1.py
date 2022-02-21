import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

def sol(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[n] = min(sol(n//3)+n%3, sol(n//2)+n%2) + 1
    return dp[n]

print(sol(n))

