import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
sample = deque(map(int,input().split()))

m = int(input())
reverseSample = deque()
for v in sample:
    if v == 1:
        reverseSample.appendleft(3)
    elif v == 2:
        reverseSample.appendleft(4)
    elif v == 3:
        reverseSample.appendleft(1)
    elif v == 4:
        reverseSample.appendleft(2)


count = 0
result = []
flag = False
for i in range(m):
    same = deque(map(int,input().split()))
    result.append(list(same))
    for j in range(n):
        same.rotate(1)
        if list(same) == list(sample) or list(same) == list(reverseSample):
            flag = True
            break
    if not flag:
        result.pop()
    flag = False

print(len(result))

for i in result:
    for v in i:
        print(v, end=" ")
    print()