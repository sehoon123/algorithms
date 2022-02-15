n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    before = 0
    for i in range(start, n):
        if not visited[i] and before != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            before = nums[i]
            dfs(i + 1)
            visited[i] = False
            temp.pop()

dfs(0)