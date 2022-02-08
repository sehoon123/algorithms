import sys
input = sys.stdin.readline

n = int(input())
length = len(str(n))

MAX = 0
for i in range(1,10):
    if int(str(i)*length) <= n:
        MAX = length
        break
    else:
        MAX = length -1

if n == 0:
    print(1)
else:
    print(MAX)
