n = int(input())

count = 0
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

# while n > 0:
#     if n - 500 >= 0:
#         n -= 500
#         count += 1
#     elif n - 100 >= 0:
#         n -= 100
#         count += 1
#     elif n - 50 >= 0:
#         n -= 50
#         count += 1
#     elif n - 10 >= 0:
#         n -= 50
#         count += 1

print(count)
# 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