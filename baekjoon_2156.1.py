import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
wines = [(int(input())) for _ in range(n)]
cache = [0] * (n + 1)

def solve(num):
    if num == 1:
        return wines[0]
    if num == 2:
        return wines[0] + wines[1]
    if num == 3:
        return max(wines[0] + wines[2], wines[1] + wines[2], wines[0] + wines[1])
    if cache[num] != 0:
        return cache[num]
    cache[num] = max(solve(num-2)+wines[num-1], solve(num-3)+wines[num-2]+wines[num-1], solve(num-1))
    return cache[num]



print(solve(n))