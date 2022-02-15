import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
parents = [0] * (n+1)

for i in range(n-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

def dfs(n):
    for i in adj[n]:
        if parents[i] == 0:
            parents[i] = n
            dfs(i)

dfs(1)
for i in range(2, n+1):
    print(parents[i])
