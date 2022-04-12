import math

n = int(input())

x = str(math.factorial(n))
result = 0

for i in range(len(x)-1, -1, -1):
    if x[i] == '0':
        result += 1
    else:
        break

print(result)

