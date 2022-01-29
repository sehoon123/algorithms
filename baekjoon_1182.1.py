n, s = map(int, input().split())
a = list(map(int, input().split()))


cnt = 0
sum = 0
def solve(i, sum):
    global cnt
    if i == n:
        return
    if sum + a[i] == s:
        cnt +=1

    solve(i+1, sum+a[i])
    solve(i+1, sum)



solve(0, sum)

print(cnt)