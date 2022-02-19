import sys
input = sys.stdin.readline

n = int(input())
price = []
time = []

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    price.append(b)

def solve(day, profit):
    v1 = profit
    v2 = profit

    if day < n:
        tI = time[day]
        pI = price[day]

        if day + tI <= n:
            v1 = solve(day + tI, profit + pI)
        if day + 1 <= n:
            v2 = solve(day + 1, profit)

    return max(v1, v2)

print(solve(0, 0))