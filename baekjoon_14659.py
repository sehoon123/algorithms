import sys
input = sys.stdin.readline

n = int(input())
mountain = list(map(int, input().split()))

CURRENT = mountain[0]
temp = 0
MAX = 0
for i in range(n):
    if CURRENT > mountain[i]:
        temp += 1
    else:
        CURRENT = mountain[i]
        MAX = max(MAX, temp)
        temp = 0

print(max(MAX,temp))
