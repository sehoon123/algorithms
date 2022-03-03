import sys
input = sys.stdin.readline

mod = int(1e9) + 7

n = int(input())
arr = list(map(int, input().split()))

result = 0
temp = 0
for i in range(n-1):
    temp = ((temp + 1) * arr[i]) % mod
    result += temp
    result %= mod

print(result % mod)
