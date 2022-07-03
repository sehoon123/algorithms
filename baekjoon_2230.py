import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(input().rstrip())
arr.sort()
left, right = 0, 1
ans = sys.maxsize

while left < n and right < n:
    tmp = arr[right] - arr[left]
    if tmp == m:
        print(m)
        exit(0)
    if tmp < m:
        right += 1
        continue
    left += 1
    ans = min(ans, tmp)

print(ans)