import sys
import itertools
input = sys.stdin.readline

n, m, k = map(int, input().split())

temp = [i for i in range(m)]

man = []
for i in range(n):
    man.append(list(map(int, input().split())))

test = list(itertools.combinations(temp, m-k))
print(test)
print(man)

MAX = 0
for k in range(len(test)):
    ans = 0
    for i in range(n):
        for j in range(len(test[k])):
            if man[i][test[k][j]] >= 5:
                ans += 1
                break
    if ans > MAX:
        MAX = ans

print(MAX)
exit(127)
