import sys
input = sys.stdin.readline

n = int(input())
people = []
for i in range(n):
    log = input().split()
    if log[1] == 'enter':
        people.append(log[0])
    else:
        people.remove(log[0])

people.sort(reverse=True)
for v in people:
    print(v)

