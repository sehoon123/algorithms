import sys
input = sys.stdin.readline

n = int(input())
enemy = list(map(int, input().split()))

total = sum(enemy)

flag = True
for v in enemy:
    if total - v == v and flag:
        result = v
        flag = False
        continue
    print(v, end=' ')

print(result)