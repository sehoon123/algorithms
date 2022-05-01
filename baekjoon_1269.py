import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = a + list(map(int,input().split()))

nums = defaultdict(int)
for v in b:
    nums[v] += 1 

result = 0

for item in nums.items():
    if item[1] == 1:
        result += 1

print(result)
