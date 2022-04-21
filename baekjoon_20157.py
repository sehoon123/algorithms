import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

arr = []
INF = 987654321
plus = int(1e9)
minus = -int(1e9)

MAX = 0

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(n):
    a, b = map(int, input().split())
    if a>0 and b > 0:
        arr.append((1, (b/gcd(a,b)),(a/gcd(a,b))))
    elif a<0 and b > 0:
        arr.append((2, (b/gcd(-a,b)),(a/gcd(-a,b))))
    elif a>0 and b < 0:
        arr.append((3, (b/gcd(a,-b)),(a/gcd(a,-b))))
    elif a<0 and b < 0:
        arr.append((4, (b/gcd(-a,-b)),(a/gcd(-a,-b))))
    elif a == 0 and b > 0:
        arr.append(INF)
    elif a == 0 and b < 0:
        arr.append(-INF)
    elif a > 0 and b == 0:
        arr.append(plus)
    elif a < 0 and b == 0:
        arr.append(minus)


cnt = Counter(arr)
print(max(cnt.values()))

