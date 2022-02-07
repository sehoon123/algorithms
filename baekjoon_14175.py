import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

pic = []
for i in range(n):
    pic.append(input().split())

for i in range(n):
    for v in pic[i]:
        for l in range(k):
            for j in range(m):
                print(v[j]*k, end='')
            print()
