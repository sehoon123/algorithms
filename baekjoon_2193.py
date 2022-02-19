n = int(input())

cache = [0] * (n + 1)

def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if cache[n] != 0:
        return cache[n]
    cache[n] = solve(n - 1) + solve(n - 2)
    return cache[n]

print(solve(n))