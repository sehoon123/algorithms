import sys
input = sys.stdin.readline

n = int(input())
cross = list(map(int, input().split()))
ll = list(map(int,input().split()))
rr = list(map(int,input().split()))
left = []
right = []
l, r = 0, 0
for i in ll:
    l += i
    left.append(l)
for i in rr:
    r += i
    right.append(r)

short = int(1e10)
index = 0
for i in range(n):
    if i == 0:
        result = cross[i] + right[-1]
    elif i == n-1 :
        result = cross[i] + left[-1]
    else:
        result = cross[i] + left[i-1] + right[-1] - right[i-1]
    if result < short:
        short = result
        index = i

print(index+1, short)


