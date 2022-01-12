import collections
n,m,v = map(int, input().split())

# edges = []
# for _ in range(m):
#     a = list(map(int, input().split()))
#     a.sort()
#     edges.append(a)
#
adj = [[] for _ in range(n+1)]
for _ in range(m):
    src, dest = map(int, input().split())
    adj[src].append(dest)
    adj[dest].append(src)

for i in range(len(adj)):
    adj[i].sort()


print(adj)

visited=[False]*(n+1)
# def dfs(adj, start, visited):
#     visited[start] = True
#     print(start, end=" ")
#     for node in adj[start]:
#         if not visited[node]:
#             dfs(adj, node, visited)
#
# dfs(adj, v, visited)

def bfs(adj, start, visited):
    visited[start] = True
    queue = collections.deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for n in adj[node]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)

bfs(adj, v, visited)
# edges.sort()
#
# visited =[False]*(n+1)
#
# def dfs(edges, start, visited):
#     visited[start] = True
#     print(start, end = " ")
#     for edge in edges:
#         if start in edge:
#             for v in edge:
#                 if not visited[v]:
#                     visited[v] = True
#                     dfs(edges, v, visited)
#
# dfs(edges, v, visited)
#
# def bfs(edges, start, visited):
#     visited[start] = True
#     queue = collections.deque()
#     queue.append(start)
#     while queue:
#         node = queue.popleft()
#         print(node, end = " ")
#         for edge in edges:
#             if node in edge:
#                 for v in edge:
#                     if not visited[v]:
#                         visited[v] = True
#                         queue.append(v)
#
#
# visited =[False]*(n+1)
# print()
# bfs(edges, v, visited)