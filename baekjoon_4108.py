import sys
input = sys.stdin.readline

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

while 1:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    graph = []
    for _ in range(r):
        graph.append(list(input().strip()))

    result = [['*'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            count = 0
            if graph[i][j] == '.':
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c:
                        if graph[nx][ny] == '*':
                            count += 1
                result[i][j] = str(count)
            else:
                result[i][j] = '*'

    for v in result:
        print(''.join(v))
