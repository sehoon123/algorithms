paren = list(input())

stack = []
tmp = 1
answer = 0

for i in range(len(paren)):

    if paren[i] == "(":
        stack.append(paren[i])
        tmp *= 2

    elif paren[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if paren[i - 1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    elif paren[i] == "[":
        stack.append(paren[i])
        tmp *= 3

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if paren[i - 1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)