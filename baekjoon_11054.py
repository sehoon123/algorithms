n = int(input())
array = list(map(int,input().split()))

da = [0] * n
dt = [0] * n

# 현재 인덱스의 원소에서의 바이토닉
for i in range(n):
    for j in range(i):
        if array[i] > array[j] and da[i] < da[j]:
            da[i] = da[j]
    da[i] += 1

test = array[::-1]

for i in range(n):
    for j in range(i):
        if test[i] > test[j] and dt[i] < dt[j]:
            dt[i] = dt[j]
    dt[i] += 1

dr = dt[::-1]

result = 0
for i in range(n):
    result = max(result, da[i] + dr[i]-1)

print(result)