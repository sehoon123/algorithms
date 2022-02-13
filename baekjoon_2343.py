import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))


def check(mid):
    total = 0
    cnt = 0
    for i in lectures:
        if i > mid:
            return False
        total += i
        if total > mid:
            cnt += 1
            total = i
    if total > 0:
        cnt += 1
    return cnt <= m


left, right = 0, int(1e9)
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)