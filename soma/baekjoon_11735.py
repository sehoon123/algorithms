import sys
input = sys.stdin.readline

n, q = map(int, input().split())

R = []
C = []
for i in range(q):
    x, y = input().split()
    y = int(y)
    total = (n**2 + n*(2*y+1))/2
    if x == 'R':
        if y in R:
            print(0)
            continue
        else:
            total -= sum(C)+y*len(C)
            R.append(y)


    elif x == 'C':
        if y in C:
            print(0)
            continue
        else:
            total -= sum(R) + y*len(R)
            C.append(y)
    print(int(total))