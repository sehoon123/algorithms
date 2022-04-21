import sys
input = sys.stdin.readline

given = list(input().strip())
n = len(given)

left = 0
right = 0
total = 0
count = 0

for i in range(n):
    if given[i] == '(':
        left += 1
        total += 1
    else:
        right += 1
        total -= 1

    if total == -1:
        count = right
        break

    if total == 1:
        left = 0

if total == 2:
    count = left

print(count)