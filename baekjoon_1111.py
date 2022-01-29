n = int(input())
a = list(map(int, input().split()))

# Ax + B
A = 0
B = 0

if n == 1:
    print("A")
    exit(0)
if (n ==2 and a[0] != a[1]):
    print("A")
    exit(0)
elif n == 2 and a[0] == a[1]:
    print(a[0])
    exit(0)

if a[0] == a[1]:
    A = 0
    B = a[1]
else:
    A = (a[2] - a[1]) // (a[1] - a[0])
    B = a[1] - A * a[0]

flag = True
print(A, B)
for i in range(1,n):
    if a[i] != A * a[i-1] + B:
        flag = False
        break


if flag:
    print(A*a[n-1] + B)
else:
    print("B")