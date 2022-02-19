from collections import deque
import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
ice = deque()
dx = [-1.0,0,1]
dy = [0, 1, -1, 0]
for i in range(n):
    temp = list(input().split())
    graph.append(temp)
    for j in range(len(temp)):
        if graph[i][j] != '0':
            ice.append([i,j,temp[j]])

tempGraph = copy.deepcopy(graph)
def bfs():
    while ice:
        count = 0
        x, y, z = ice.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '0':
                    count += 1


                    



