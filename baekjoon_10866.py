from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        q.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        q.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        try:
            print(q.popleft())
        except:
            print(-1)
    elif cmd[0] == 'pop_back':
        try:
            print(q.pop())
        except:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    elif cmd[0] == 'back':
        try:
            print(q[-1])
        except:
            print(-1)
