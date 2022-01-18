n = int(input())
array = [0] * 500

for _ in range(n):
    a, b = map(int, input().split())
    array[a-1] = b

refined = [x for x in array if x != 0]

d = [0] * 500
for i in range(len(refined)):
    for j in range(i):
        if refined[i] > refined[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

result = max(d)

print(n - result)