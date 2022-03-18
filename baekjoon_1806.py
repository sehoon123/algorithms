import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int,input().split()))
arr = [0] * (n+1)

start, end = 0, 0
flag = True
for i in range(1,n+1):
    arr[i] = arr[i-1] + nums[i-1]
    if flag and arr[i] >= s:
        end = i
        flag = False


result = end

while end <= n:
    start += 1
    while end <= n and arr[end] - arr[start] < s:
        end += 1

    if end - start < result:
        result = end - start

print(result)
