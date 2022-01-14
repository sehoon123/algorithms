n, m = map(int, input().split())

visited = [0] * (n + 1)
array = []
count = 0

def dfs():
    if len(array) == m:
        print(' '.join(map(str, array)))
        return

    for i in range(1, n+1):
        if visited[i]== 1:
            continue
        visited[i] = 1
        array.append(i)
        dfs()
        array.pop()
        for j in range(i+1, n+1):
            visited[j] = 0

dfs()