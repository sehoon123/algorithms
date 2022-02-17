import sys
input = sys.stdin.readline

n = int(input())

def check(a):
    stack = []
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(a[i])
        elif a[i] == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

for _ in range(n):
    a = input().strip()
    if check(a):
        print('YES')
    else:
        print('NO')


