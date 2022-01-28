T = int(input())

d =[0]*31
def fact(n):
    d[0] = 1
    for i in range(1, n+1):
        d[i] = d[i-1] * i
    return d[n]

for i in range(T):
    a, b = map(int, input().split())
    print(fact(b) // (fact(b-a) * fact(a)))


