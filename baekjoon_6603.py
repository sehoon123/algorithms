import sys
import itertools
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr.pop(0)
    result = itertools.combinations(arr, 6)
    for i in result:
        print(*i)
    print()