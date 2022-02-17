import sys
input = sys.stdin.readline

def f(c):
    if c == m:
        print(' '.join(ans))
        return
    t = -1
    for j in range(n):
        if visit[j] or t == ls[j]:
            continue
        visit[j] = 1
        ans.append(ls[j])
        f(c+1)
        visit[j] = 0
        t = ans.pop()

n, m = map(int, input().split())
ls = input().split()
ls.sort(key=int)
ans, visit = [], [0]*n
f(0)