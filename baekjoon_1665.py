import sys
# import bisect
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
arr = PriorityQueue()

for i in range(n):
    arr.put(int(input()))
    print(list(arr))


