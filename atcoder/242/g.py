import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

t = int(input())
for _ in range(t):
    total = 0
    l, r = map(int, input().split())
    result = Counter(arr[l-1:r+1])
    for v in result:
        total += result[v]//2
    print(total)