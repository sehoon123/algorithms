import itertools
n, s = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    b = list(itertools.combinations(a, i))
    for j in b:
        if sum(j) == s:
            count += 1

print(count)