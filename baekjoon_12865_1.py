n, k = map(int, input().split())

item = []

for i in range(n):
    w, v = map(int, input().split())
    item.append((w, v))

d = [[0] * (101) for _ in range(100001)]
def knapsack(i, w):
    if d[i][w] > 0:
        return d[i][w]
    if i == n:
        return 0
    n1 = 0
    if w + item[i][0] <= k:
        n1 = item[i][1] + knapsack(i+1, w + item[i][0])
    n2 = knapsack(i+1, w)

    d[i][w] = max(n1, n2)
    return d[i][w]

print(knapsack(0,0))

