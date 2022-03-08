import sys
input = sys.stdin.readline

n = int(input())
village = []
for i in range(n):
    village.append(list(map(int,input().split())))

village.sort()
cum = [0]*n
cum[0] = village[0][1]

for i in range(1,n):
    cum[i] = cum[i-1] + village[i][1]

left = 0
right = n-1
pos = int(1e12)

while left <= right:
    mid = (left+right)//2
    lsum = cum[mid]
    rsum = cum[n-1]-cum[mid]
    if lsum >= rsum:
        right = mid -1
        pos = min(pos,village[mid][0])
    else:
        left = mid + 1

print(pos)
