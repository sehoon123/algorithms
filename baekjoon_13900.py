import sys
input = sys.stdin.readline

input()
nums = list(map(int, input().split()))
s = sum(nums)
ans = 0
for n in nums:
    s = s - n
    ans += n * s

print(ans)