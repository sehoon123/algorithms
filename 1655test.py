import sys
import heapq
input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
heap1 = []
heap2 = []
for i in range(n):
    heapq.heappush(heap1, -nums[i])
    if i % 2 == 1:
        a = heapq.heappop(heap1)
        heapq.heappush(heap2, -a)

    if heap2 and -heap1[0] > heap2[0]:
        a = heapq.heappop(heap1)
        b = heapq.heappop(heap2)
        heapq.heappush(heap2, -a)
        heapq.heappush(heap1, -b)
    print(-heap1[0])
