n = int(input())
list_a = list(map(int, input().split()))

list_a.sort()

count = 0

for i in list_a:
    for j in range(i):
        list_a.remove(list_a[0])
    count += 1

print(count)