import sys
import heapq

input = sys.stdin.readline
n, l = map(int, input().split())
arr = list(enumerate(map(int,input().split())))

print(arr)

q = []

for i in range(n):
    heapq.heappush(q, (arr[i][1], arr[i][0]))
    idx = q[0][1]
    while idx < i-l+1:
        heapq.heappop(q)
        idx = q[0][1]
    print(q)