n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    b = b % 4 + 4
    result = a ** b
    if result % 10 == 0:
        print(10)
    else:
        print(result % 10)