n, k = map(int, input().split())

w = [0 for _ in range(101)]
v = [0 for _ in range(101)]


for i in range(n):
    a, b = map(int, input().split())
    w[i] = a
    v[i] = b

d = [[0] * (101) for _ in range(100001)]
def knapsack(a, b):
    if d[a][b] > 0:
        return d[a][b]
    if i == n:
        return 0
    n1 = 0
    if b + w[a] <= k:
        n1 = w[a] + knapsack(i+1, b + w[a])
    n2 = knapsack(a+1, b)

    d[a][b] = max(n1, n2)
    return d[a][b]

print(knapsack(0,0))

