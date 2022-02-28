import math

n = int(input())
word = input()
# m = len(word)
m = 3000
MOD = 1000000007

def pp(a, p, MOD):
    if p == 1:
        return a
    b = pp(a, p//2, MOD)
    if(p % 2 == 0):
        return(b*b) % MOD
    else:
        return(((b*b) % MOD) * a) % MOD

f = [0] * (6001)
f[0] =1
f[1] =1
for i in range(2, 6001):
    f[i] = i * f[i-1] % MOD

N = m+n-1
K = n
print(f[N]*pp((f[K]*f[N-K])%MOD,MOD-2,MOD)%MOD)

