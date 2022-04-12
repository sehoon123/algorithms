import sys
import heapq

input = sys.stdin.readline
n = int(input())
min_heap = []
max_heap = []
for _ in range(n):
    now = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-now, now))
    else:
        heapq.heappush(min_heap, (now, now))

    if min_heap and min_heap[0][1] < max_heap[0][1]:
        aaa = heapq.heappop(min_heap)[1]
        bbb = heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, (bbb, bbb))
        heapq.heappush(max_heap, (-aaa, aaa))
    print(max_heap[0][1])
    

