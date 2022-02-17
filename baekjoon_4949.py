import sys
import re
input = sys.stdin.readline

def check(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) == 0:
                return False
            if stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) == 0

while True:
    string = input().rstrip()
    if string == '.':
        break
    string = re.findall(r'[\(,\),\[,\]]', string)

    if check(string):
        print('yes')
    else:
        print('no')