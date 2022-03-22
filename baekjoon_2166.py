import sys
input = sys.stdin.readline
x = []
y = []

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x = x + x
y = y + y

temp1= 0
temp2 = 0
for i in range(n):
    temp1 += x[i] * y[i+1]
    temp2 += y[i] * x[i+1]

print("%.1f" %(abs(temp1 - temp2) / 2))