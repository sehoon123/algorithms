import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

MAX = 10

N, M = map(int, input().split())
adj = [[] for _ in range(MAX)]
comp = [[] for _ in range(MAX)]
string = [[] for _ in range(MAX)]
s = input().strip()
num = 0

for i in range(1, N+1):
    string[i] = s[i - 1]


for i in range(N-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

def dfs(x):
    if comp[x]:
        return
    comp[x] = num
    for v in adj[x]:
        if string[v] == string[x]:
            dfs(v)



for i in range(1, N+1):
    if not comp[i]:
        num += 1
        dfs(i)

for i in range(M):
    a, b, c = input().split()
    if string[int(a)] == c or comp[int(a)] != comp[int(b)]:
        print(1,end="")
    else:
        print(0,end="")
