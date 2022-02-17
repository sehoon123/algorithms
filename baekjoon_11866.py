from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])
result = []

while len(q) > 0:
    q.rotate(-(k-1))
    result.append(q.popleft())


print('<', end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print('>')