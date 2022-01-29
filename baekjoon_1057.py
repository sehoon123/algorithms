n, a, b = map(int, input().split())

count = 0

while True:
    if ((a+1)//2) == ((b+1)//2):
        count += 1
        print(count)
        break
    a = (a+1)//2
    b = (b+1)//2
    count += 1