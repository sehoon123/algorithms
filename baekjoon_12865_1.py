n, k = map(int, input().split())

w = [0] * 101
v = [0] * 101


for i in range(n):
    a, b = map(int, input().split())
    w[i] = a
    v[i] = b

cache = [[0] * (100001) for _ in range(101)]
def knapsack(i, weight):
    if cache[i][weight] > 0:
        return cache[i][weight]
    if i == n:
        return 0
    n1 = 0
    if weight + w[i] <= k:
        n1 = v[i] + knapsack(i + 1, weight + w[i])
    n2 = knapsack(i + 1, weight)

    cache[i][weight] = max(n1, n2)
    return cache[i][weight]

print(knapsack(0,0))

