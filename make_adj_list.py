n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for i in range(m):
    src, dest = map(int, input().spilt())
    adj[src].append(dest)
    adj[dest].append(src)

for i in range(len(adj)):
    adj[i].sort