import sys
# input = sys.stdin.readline().rstrip
n = int(input())
parts = list(map(int,input().split()))

m = int(input())
demand = list(map(int,input().split()))

for i in demand:
    if not parts.__contains__(i):
        print("NO", end=" ")
    else:
        print("YES", end=" ")


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
        return None