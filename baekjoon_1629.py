import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

def mod(a, b):
    if b == 1:
        return a % c

    ans = mod(a, b//2)
    if b % 2 != 0:
        return ans * ans * a % c
    else:
        return ans * ans % c

print(mod(a, b))
