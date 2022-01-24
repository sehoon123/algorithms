n = int(input())
A = list(map(int, input().split()))
lis = []

def upperbound(A, x):
    start, end = 0, len(A)-1
    while start < end:
        mid = (start + end) // 2
        if A[mid] >= x:
            end = mid
        else:
            start = mid + 1
    return start

lis.append(A[0])
for i in range(1, n):
    if A[i] > lis[-1]:
        lis.append(A[i])
    else:
        k = upperbound(lis, A[i])
        lis[k] = A[i]

print(len(lis))