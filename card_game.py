n, m = map(int, input().split())

result = 0
for _ in range(n):
    temp = min(list(map(int, input().split())))
    if temp > result:
        result = temp

print(temp)