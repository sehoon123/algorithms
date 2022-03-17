import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
jewel = [0] * m
total = 0

for i in range(m):
    jewel[i] = int(input())
    total += jewel[i]

left, right = 1, total
ans = 0

def check(mid):
    if mid > total:
        return False
    temp = n
    for i in range(m):
        if mid < jewel[i]:
            temp -= math.ceil(jewel[i] / mid)
        else:
            temp -= 1
    return temp >= 0



while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)