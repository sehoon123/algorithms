import sys
input = sys.stdin.readline

n, q = map(int, input().split())
cows = list(map(int, input().split()))
fake = list(map(int, input().split()))

memo = [0] * n

original = 0
for i in range(n):
    memo[i] = cows[i]*cows[i-1]*cows[i-2]*cows[i-3]

original = sum(memo)

for v in fake:
    for i in range(4):
        idx = (v-1+i) % n
        memo[idx] = - memo[idx]
        original += 2 * memo[idx]
    print(original)