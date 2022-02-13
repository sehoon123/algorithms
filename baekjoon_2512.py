import sys

input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
maximum_budget = int(input())


def check(mid):
    total = 0
    for budget in budgets:
        if budget > mid:
            total += mid
        else:
            total += budget

    return total <= maximum_budget


if sum(budgets) <= maximum_budget:
    print(max(budgets))
else:
    left, right = 1, int(1e9)
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    print(right)
