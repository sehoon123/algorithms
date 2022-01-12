from collections import deque

n, m = map(int, input().split())

graph = [1]*(100001)

queue = deque()
queue.append(n)


def bfs():
    while queue:
        x = queue.popleft()
        if x == m:
            print(graph[x]-1)
            break
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and graph[nx] == 1:
                graph[nx] = graph[x] + 1
                queue.append(nx)


bfs()
