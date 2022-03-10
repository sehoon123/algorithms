import sys
input = sys.stdin.readline

num = int(input())
result = []
stack = []
cnt = 0

flag = True

for i in range(num):
    now = int(input())

    while cnt < now:
        cnt += 1
        result.append("+")
        stack.append(cnt)

    if stack[-1] == now:
        result.append("-")
        stack.pop()
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for v in result:
        print(v)
