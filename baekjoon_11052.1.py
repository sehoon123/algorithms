import sys
input = sys.stdin.readline

n = int(input())
cards= list((map(int, input().split())))

cache = [0] * (n+1)

def solve(n):
    if n == 1:
        return cards[0]
    if cache[n] != 0:
        return cache[n]
    for i in range(n):
        cache[n] = max(cache[n], solve(i) + cards[n-i-1])
    return cache[n]

print(solve(n))

