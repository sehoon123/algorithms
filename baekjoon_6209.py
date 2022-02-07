import sys
input = sys.stdin.readline

d, n, m = map(int, input().split())
island = [0] * (n + 2)
island[0] = 0
island[n + 1] = d

for i in range(1, n+1):
    island[i] = int(input())

island.sort()

def binary(left, right):
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid -1

    return ans


def check(mid):
    count = 0
    start = 0
    for i in range(1, n+2):
        if island[i] - start < mid:
            count += 1
        else:
            start = island[i]
    return count <= m

# if n == 0:
#     print(d)
#     exit(0)
result = binary(1, d)
print(result)