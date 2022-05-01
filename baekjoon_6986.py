import sys
input = sys.stdin.readline

n, m = map(int,input().split())
scores = []

for _ in range(n):
    x = input().split()
    scores.append(float(x[0]))

scores.sort()

trimmed_mean = sum(scores[m:n-m])/(n-2*m)+(1e-8)
print(f'{trimmed_mean:.2f}')
mean = ((sum(scores[m:n-m]) + scores[m]*m + scores[n-m-1]*m)/n) + (1e-8)
print(f'{mean:.2f}')