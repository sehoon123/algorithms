n, k = map(int, input().split())

money_list = []
for _ in range(n):
    money_list.append(int(input()))

money_list.sort(reverse=True)
count = 0

while k != 0:
    for v in money_list:
        if k >= v:
            count += k//v
            k = k - (v) * (k // v)

print(count)