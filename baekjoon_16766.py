import sys

input = sys.stdin.readline

# n : number of cows, m : number of buses, c : capacity of bus
n, m, c = map(int, input().split())

arrival = list(map(int, input().split()))
arrival.sort()

left = 0
# right = int(1e9 + 1)
right = arrival[-1]


def binary(left, right):
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


def check(mid):
    count = 1
    start = 0
    for i in range(1, n):
        if i - start < c and arrival[i] - arrival[start] <= mid:
            continue
        count += 1
        start = i

    return count <= m


result = binary(left, right)
print(result)
