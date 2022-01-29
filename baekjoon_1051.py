import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(input())

result = 0
for i in range(n):
    for j in range(m):
        for k in range(n):
            if i + k >= n or j + k >= m :
                continue
            if a[i][j] == a[i+k][j+k] and a[i][j] == a[i+k][j] and a[i][j] == a[i][j+k]:
                result = max(result, k+1)

print(result**2)