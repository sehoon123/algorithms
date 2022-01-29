start, end = map(int, input().split())
a = []

for i in range(1, end + 1):
    if len(a) > end + 1:
        break
    for j in range(i):
        a.append(i)

print(sum(a[start - 1:end]))