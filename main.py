n = int(input())

count = 0

while n > 0:
    if n - 500 >= 0:
        n -= 500
        count += 1
    elif n - 100 >= 0:
        n -= 100
        count += 1
    elif n - 50 >= 0:
        n -= 50
        count += 1
    elif n - 10 >= 0:
        n -= 50
        count += 1

print(count)
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
