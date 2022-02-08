import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_total = 0
B_total = 0

flag = False

for i in range(9):
    A_total += A[i]
    if A_total > B_total:
        flag = True

    B_total += B[i]
    if A_total > B_total:
        flag = True

if flag and A_total < B_total:
    print("Yes")
else:
    print("No")