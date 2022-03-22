import heapq
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

q = []
for i in range(k):
    a,b = map(int, input().split())
    heapq.heappush(q, (a,b))
    if len(q) > n:
        heapq.heappop(q)

def check(mid):
    pref = 0
    count = 0
    for i in range(k):
        if q[i][1] <= mid:
            pref += -q[i][0]
            count += 1
        if count == n:
            break

    return pref >= m

left, right = 0, 1<<31
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid -1
        ans = mid
    else:
        left = mid + 1

if ans == 0:
    print(-1)
else:
    print(ans)