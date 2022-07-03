n = int(input())
now = 0
for i in range(n):
    num = int(input())
    if num % 2 == 1:
        now += num
    print(now)