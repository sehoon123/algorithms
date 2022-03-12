import sys
input = sys.stdin.readline

stack = []
result = 0

paren = input().rstrip()
for i in range(len(paren)):
    if paren[i] == '(':
        stack.append(paren[i])
    else:
        if paren[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)