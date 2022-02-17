import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * (n)
result = []
temp = set()


def dfs(n, m):
    if len(result) == m:
        temp.add(tuple(result))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            dfs(n, m)
            visited[i] = False
            result.pop()


dfs(n, m)

for v in sorted(temp):
    print(*v)

