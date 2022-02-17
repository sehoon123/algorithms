import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(set(map(int, input().split())))

visited = [False] * (n)
result = []


def dfs(n, m):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(len(arr)):
        if not visited[i]:
            result.append(arr[i])
            dfs(n, m)
            result.pop()


dfs(n, m)

