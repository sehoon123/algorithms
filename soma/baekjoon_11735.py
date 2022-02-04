n, q = map(int, input().split())
R = [0] * (n+1)
C = [0] * (n+1)

for i in range(q):
    x, y = input().split()
    y = int(y)
    total = (n**2 + n*(2*y+1))/2
    if x == 'R':
        if R[y] == 1:
            print(0)
            continue
        for i in range(1,n+1):
            if C[i] == 1:
                total -= (y+i)
        R[y] = 1

    elif x == 'C':
        if C[y] == 1:
            print(0)
            continue
        for i in range(1, n+1):
            if R[i] == 1:
                total -= (y + i)
        C[y] = 1

    print(int(total))