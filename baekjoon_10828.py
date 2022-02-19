import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    msg = input().split()
    if msg[0] == "push":
        ele = int(msg[1])
        stack.append(ele)
    elif msg[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif msg[0] == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    elif msg[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif msg[0] == "size":
        print(len(stack))
