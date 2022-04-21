import sys
from collections import defaultdict

input = sys.stdin.readline
que = defaultdict(int)

k, l = map(int, input().split())

for i in range(l):
    que[input().strip()] = i

sorted_que = sorted(que.items(), key=lambda x:x[1])

for i in range(k):
    try:
        print(sorted_que[i][0])
    except:
        break