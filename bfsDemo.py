#bfs use Queue

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

visited = [False] * len(graph)
bfs(graph,1,visited)