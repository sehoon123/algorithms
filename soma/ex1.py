n = int(input())
a = list(map(int, input().split()))

def develop(start, end):
    if start + 1 == end:
        return max(a[start], a[end])
    mid = (start + end) // 2
    leftMax, rightMax = 0, 0
    for i in range(start, mid+1):
        leftMax = max(leftMax, a[i])
    for i in range(mid+1, end+1):
        rightMax = max(rightMax, a[i])

    return max(leftMax + develop(mid+1, end), rightMax + develop(start, mid))

print(develop(0, n-1))