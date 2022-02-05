import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snack = list(map(int, input().split()))


def possible(mid, snack):
    total = 0
    for i in range(N):
        total += snack[i] // mid

    return total >= M

def binary(left, right):
    while left <= right:
        mid = (left + right) // 2
        if possible(mid, snack):
            left = mid + 1
        else :
            right = mid - 1

    return right

result = binary(1, 1000000001)
print(result)
