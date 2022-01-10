def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],    # Edge from 1
    [1,7],      # Edge from 2
    [1,4,5],    # Edge from 3
    [3,5],      # Edge from 4
    [3,4],      # Edge from 5
    [7],        # Edge from 6
    [2,6,8],    # Edge from 7
    [1,7],       # Edge from 8
]

visited = [False] * 9
dfs(graph, 1, visited)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)