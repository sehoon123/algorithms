import sys
input = sys.stdin.readline

n,k,m = map(int, input().split())
kim = [0]*n
temp_max = 0
for i in range(n):
    kim[i] = int(input())
    if kim[i] > temp_max:
        temp_max = kim[i]

def check(mid):
    count = 0
    for i in range(n):
        if kim[i] >=2 * k:
            remain = kim[i] - 2 * k
            count += remain // mid
        elif k < kim[i] < 2 * k:
            remain = kim[i] - k
            count += remain // mid
    return count >= m

ans = 0
left, right = 1, temp_max
while left <= right:
    mid = (left+right)//2
    if check(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

if ans == 0:
    print(-1)
else:
    print(ans)


