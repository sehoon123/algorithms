import sys
input = sys.stdin.readline

cache = [0] * 11

t = int(input())

def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    if cache[n] != 0:
        return cache[n]
    cache[n] = solve(n-1)+solve(n-2)+solve(n-3)
    return cache[n]




for _ in range(t):
    n = int(input())
    print(solve(n))