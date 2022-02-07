import sys
input = sys.stdin.readline

n = int(input())

tread = [[] for _ in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    tread[i] = [a, a+b]

tread.sort(key=lambda x: x[0])

answer = 0
left = 1
right = 20000000000
while(left <= right):
    mid = (left + right) // 2
    knot = tread[0][0]
    flag = 0
    for v in tread:
        if knot >= v[0] and knot <= v[1]:
            knot += mid
        elif knot < v[0]:
            knot = v[0] + mid
        else:
            flag = 1
            break

    if flag == 0:
        if mid > answer:
            answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)