n, k = map(int, input().split())

item = []
for i in range(n):
    w, v = map(int, input().split())
    item.append((w, v))

# print(item)

d = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
       if j >= item[i-1][0]:
           d[i][j] = max(d[i-1][j], d[i-1][j-item[i-1][0]] + item[i-1][1])
       else:
           d[i][j] = d[i-1][j]


for v in d:
    print(v)