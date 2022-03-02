import math
a, b, c = map(int, input().split())

if c / 5 > b:
    print(1)
    exit()
else:
    temp = 1
    for i in range(math.ceil(c/5)):
        temp *= b/a
        a-=1
        b-=1

print(1-temp)

