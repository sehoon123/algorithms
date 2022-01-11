from collections import deque
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for w in graph[node]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for w in graph[node]:
            if not visited[w]:
                visited[w] = True
                deque.append(w)





def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        for node in graph[start]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)




def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for e in graph[node]:
            if not visited[e]:
                visited[e] = True
                queue.append(e)












