from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

visited = [[[False] * m for _ in range(n)] for _ in range(2)]
visited[0][0][0] = True
visited[1][0][0] = True


queue = deque()
queue.append([0,0,1,1])


dx = [0,0,1,-1]
dy = [1,-1,0,0]

while queue:
   x, y, chance, distance= queue.popleft()
   if x == n-1 and y == m-1:
       result = distance
       break
   for i in range(4):
       nx = x + dx[i]
       ny = y + dy[i]
       if 0 <= nx < n and 0 <= ny < m and not visited[chance][nx][ny]:
           if graph[nx][ny] == 1 and chance == 1:
               chance = 0
               visited[chance][nx][ny] = True
               queue.append([nx,ny, chance, distance+1])
           elif graph[nx][ny] == 0:
               visited[chance][nx][ny] = True
               queue.append([nx, ny, chance, distance + 1])

else :
    result = -1

if n == 1 and m == 1:
    print(1)
else:
    print(result)


