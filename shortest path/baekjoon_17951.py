import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = list(map(int, input().split()))

left, right = 0, 1000000000


def binary(left, right):
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right


def check(mid):
    cnt = 0
    total = 0
    for i in range(n):
        total += score[i]
        if total >= mid:
            cnt += 1
            total = 0

    return cnt >= k


result = binary(left, right)
print(result)