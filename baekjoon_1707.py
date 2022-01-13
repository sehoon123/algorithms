from collections import deque

def bfs(adj, start, visited, color):
    color[start] = 1
    visited[start] = 1
    queue = deque()
    queue.append([start, color[start]])
    flag = True
    while queue:
        node, col = queue.popleft()
        for u in adj[node]:
            if visited[u] == 0:
                visited[u] = 1
                if col == 1:
                    color[u] = -1
                else:
                    color[u] = 1
                queue.append([u, color[u]])
            if color[u] == col:
                flag = False
                break

    if flag:
        return True
    else:
        return False

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    visited = [0]*(V+1)
    color = [0]*(V+1)
    adj = [[] for _ in range(V+1)]
    flag = True
    for i in range(E):
        src, dest = map(int, input().split())
        adj[src].append(dest)
        adj[dest].append(src)


    for i in range(1, V+1):
        if visited[i] == 0:
            if not bfs(adj, i, visited, color):
                flag = False
                break

    if flag:
        print("YES")
    else:
        print("NO")

#####################################

# import sys
#
# input = sys.stdin.readline
# from collections import deque
#
#
# def bfs(x):
#     visited[x] = 1
#     q = deque()
#     q.append(x)
#     while q:
#         a = q.popleft()
#         for i in que[a]:
#             if visited[i] == 0:
#                 visited[i] = -visited[a]
#                 q.append(i)
#             else:
#                 if visited[i] == visited[a]:
#                     return False
#     return True
#
#
# k = int(input())
# for i in range(k):
#     v, e = map(int, input().split())
#     que = [[] for i in range(v + 1)]
#     visited = [0] * (v + 1)
#     flg = 1
#     for j in range(e):
#         a, b = map(int, input().split())
#         que[a].append(b)
#         que[b].append(a)
#     for k in range(1, v + 1):
#         if visited[k] == 0:
#             if not bfs(k):
#                 flg = -1
#                 break
#
#     print('YES' if flg == 1 else 'NO')