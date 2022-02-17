import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    ele = int(input())
    if ele == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)*-1)
    else:
        heapq.heappush(heap, -ele)

