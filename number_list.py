# n, m, k = map(int, input().split())
n = 5
m = 8
k = 3

# data = list(map(int,input().split()))

data = [2,4,5,4,6]

data.sort(reverse=True)

result = 0
count = 0
for i in range(m):
    if count == k:
        count = 0
        result += data[1]
        continue

    count += 1
    result += data[0]

print(result)