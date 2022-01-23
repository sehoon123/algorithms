import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
a = {}
for i in range(n):
    if A[i] in a:
        a[A[i]] += 1
    else:
        a[A[i]] = 1

m = int(input())
B = list(map(int, input().split()))

for i in range(m):
    if B[i] in a:
        print(a[B[i]], end=' ')
    else:
        print(0, end=' ')