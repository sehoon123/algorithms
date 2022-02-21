import sys
input = sys.stdin.readline


while True:
    n, m = map(float, input().split())
    n = int(n)
    if n == 0 and m == 0.00:
        break
    m = int(m * 100)
    candy = []
    cache = [0] * (m + 1)
    for i in range(n):
        c, p = map(float, input().split())
        candy.append((int(c), int(p*100)))

    for i in range(1, n+1):
        for j in range(candy[i-1][1], m+1):
            cache[j] = max(cache[j], cache[j-candy[i-1][1]] + candy[i-1][0])

    print(cache[m])

