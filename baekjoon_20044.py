n = int(input())
arr = list(map(int,input().split()))

arr.sort()
MIN = 1e9
left = n
right = n-1

for i in range(n):
    left -= 1
    right += 1
    temp = arr[left]+arr[right]
    if MIN > temp:
        MIN = temp

print(MIN)
