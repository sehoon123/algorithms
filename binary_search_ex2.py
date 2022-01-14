import sys


n, m = map(int, input().split())
array= list(map(int, sys.stdin.readline().split()))
array.sort()

def binary_search(start, end, target):
    sum = 0
    mid = (start + end) // 2
    h = mid
    for a in array:
        if a > h:
            sum += a-h
    if sum == target:
        return h
    elif sum > target:
        return binary_search(mid+1, end, target)
    else:
        return binary_search(start, mid-1, target)


print(binary_search(min(array), max(array), m))




