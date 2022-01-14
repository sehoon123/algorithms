n = 26

count = 0
while n > 0:
    if n == 1:
        break
    if n % 5 == 0:
        count += 1
        n = n / 5
    elif (n-1) % 5 == 0:
        count += 2
        n = (n-1)/5
    elif n % 3 == 0:
        count += 1
        n = n / 3
    elif (n-1) % 3 == 0:
        count += 2
        n = (n-1)/3
    elif n % 2 == 0:
        count += 1
        n = n / 2
    elif (n-1) % 2 == 0:
        count += 2
        n = n / 2
    else:
        n = n - 1
        count += 1

print(count)