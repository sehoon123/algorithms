import sys
input = sys.stdin.readline

cache = [0] * 41

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if cache[n] != 0:
        return cache[n]
    cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]

n = int(input())
num = [int(input()) for _ in range(n)]

for i in num:
    if i == 0:
        print(1, 0)
    else:
        print(fibo(i-1), fibo(i))