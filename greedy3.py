n = int(input())
list_a = list(map(int, input().split()))

list_a.sort()

count = 0
result = 0

for i in list_a:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)