for _ in range(int(input())):
    n = input()
    reverse = ""
    for i in range(len(n)):
        reverse += str(9 - int(n[i]))
    if int(n) <= 10**len(n)//2:
        result = int(n) * int(reverse)
    else:
        result = (10**len(n)//2) * ((10**len(n)//2) - 1)

    print(result)

