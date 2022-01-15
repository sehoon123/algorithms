n, m = map(int, input().split())
money_list = []
for _ in range(n):
    money_list.append(int(input()))

d = [0] * 10001
for v in money_list:
    d[v] = 1

for i in range(1, m+1):
    pivot = 1e9
    for k in money_list:
        if i - k >= 0 and d[i-k] != 0:
            pivot = min(pivot, d[i-k] + d[k])
            d[i] = pivot

if d[m] == 0 :
    print(-1)
else:
    print(d[m])

