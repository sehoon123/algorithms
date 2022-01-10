from collections import deque
#dfs
def dfs(graph, v, visited):
    visited[v] = True
    print("%d ", v)
    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            dfs(graph, u, visited)

#bfs
def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
