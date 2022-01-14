n, m = map(int, input().split())

s = []
visited = [0] * (n + 1)
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            s.append(i)
        else:
            continue
        dfs()
        k = s.pop()
        visited[k] = 0

dfs()
