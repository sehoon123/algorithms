n, k = map(int, input().split())
products = []
for _ in range(n):
    w, v = map(int, input().split())
    products.append((w,v))

d = [0] * (k+1)
for w, v in products:
    for i in range(k, w-1, -1):
        d[i] = max(d[i], d[i-w] + v)

print(d[-1])
