n = int(input())
graph = []
for _ in range(n):
    graph.append(input())


row = 0
column = 0
count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == '.':
            count += 1
        if graph[i][j] == 'X' or j == n - 1:
            if count >= 2:
                row += 1
            count = 0

for i in range(n):
    for j in range(n):
        if graph[j][i] == '.':
            count += 1
        if graph[j][i] == 'X' or j == n - 1:
            if count >= 2:
                column += 1
            count = 0

print(row, column)
