n = int(input())
cargo = list(map(int, input().split()))

d = [0] * 100

d[0] = cargo[0]
d[1] = cargo[1]

for i in range(2, n):
    d[i] = max(d[i-2] + cargo[i], d[i-3] + cargo[i - 1], d[i-3] + cargo[i])

print(d[n-1])