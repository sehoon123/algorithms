from collections import deque
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    cnt = 0
    n, m = map(int, input().split())
    q = deque()
    arr = list(map(int,input().split()))
    for i in range(n):
        q.append([i, arr[i]])
    while q:
        for i in range(len(q)):
            p_now = q[0][1]
            if q[i][1] > p_now:
                q.rotate(-1)
                break
        else:
            first = q.popleft()
            cnt += 1
            if first[0] == m:
                print(cnt)



