# def fibo(n):
#     if n <= 2:
#         return 1
#     if memo[n] != 0:
#         return memo[n]
#     memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]
#
# n = int(input())
#
# memo = [0] * (n + 1)
# result = fibo(n)
# print(memo)
# print(result)


n = 99
d = [0] * (n + 1)
d[1] = 1
d[2] = 1

for i in range(3,n+1):
    d[i] = d[i-2] + d[i-1]
print(d[n])
