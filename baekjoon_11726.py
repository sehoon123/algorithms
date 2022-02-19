n = int(input())
cache = [0] * (n + 1)


def tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if cache[n] != 0:
        return cache[n]
    cache[n] = tile(n - 1) + tile(n - 2)
    return cache[n]


print(tile(n)%10007)

