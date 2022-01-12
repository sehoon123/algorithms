from collections import deque
n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n+1)
# def bfs(adj, start, visited):
#     visited[start] = True
#     queue = deque()
#     queue.append(start)
#     count = 0
#     while queue:
#         cur = queue.popleft()
#         count += 1
#         for i in adj[cur]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#     return count-1
#
# print(bfs(adj, 1, visited))

def dfs(adj, start, visited):
    visited[start] = True
    for i in adj[start]:
        if not visited[i]:
            dfs(adj, i, visited)

dfs(adj, 1, visited)
print(visited.count(True)-1)