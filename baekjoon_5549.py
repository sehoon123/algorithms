import sys
input = sys.stdin.readline

n, m = map(int,input().split())
k = int(input())

temp = []
graph = [[0]*m for _ in range(n)]
dp = [[[0]*3 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    temp = input().strip()
    for j in range(m):
        graph[i][j] = temp[j]

for i in range(n):
    J, O, I = 0,0,0
    for j in range(m):
        if graph[i][j] == 'J':
            J += 1
        elif graph[i][j] == 'O':
            O += 1
        elif graph[i][j] == 'I':
            I += 1
        dp[i+1][j+1][0] = J
        dp[i+1][j+1][1] = O
        dp[i+1][j+1][2] = I


for _ in range(k):
    a,b,c,d = map(int, input().split())
    J, O, I = 0,0,0
    for i in range(a,c+1):
        J += dp[i][d][0] - dp[i][b-1][0]
        O += dp[i][d][1] - dp[i][b-1][1]
        I += dp[i][d][2] - dp[i][b-1][2]
    print(J, O, I)
