import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[[0] * 3 for i in range(4)] for j in range(N + 1)]
pasta = [0] * (N + 1)
for i in range(K):
    a, b = map(int, input().split())
    pasta[a] = b

# dp[day][pasta][continuous]
if pasta[1]:
    dp[1][pasta[1]][1] = 1
else:
    dp[1][1][1] = dp[1][2][1] = dp[1][3][1] = 1

for i in range(2, N + 1):
    if pasta[i] != 0:
        for j in range(1, 4):
          #정해진 음식을 처음먹을떄를 카운트 하기 때문에 이 음식을 먹었던 경우는 제외한다.
            if j == pasta[i]:
                continue
            # 정해진 음식을 처음 먹는 경우의 수는 전 날 다른음식을 처음먹은경우와 다른음식을 2번연속먹은경우를 모두 더한것이다.
            dp[i][pasta[i]][1] += dp[i - 1][j][1] + dp[i - 1][j][2]
            dp[i][pasta[i]][1] %= 10000
        # 정해진 음식을 다음날까지 먹는 경우는 1가지밖에 없음 즉, 전날과 같음
        dp[i][pasta[i]][2] = dp[i - 1][pasta[i]][1]
    else:
        for j in range(1, 4):
            #음식을 2일 연속 먹는 방법은 1가지밖에 없음
            dp[i][j][2] = dp[i - 1][j][1]
            for k in range(1, 4):
                if j == k:
                    continue
                dp[i][j][1] += dp[i - 1][k][1] + dp[i - 1][k][2]
                dp[i][j][1] %= 10000

# N일째 되는날 1번 파스타를 1일연속먹은경우, 2일연속먹은경우, 2번파스타를 1일연속 먹은경우, 2일연속 먹은경우, ...
print((dp[N][1][1] + dp[N][1][2] + dp[N][2][1] + dp[N][2][2] + dp[N][3][1] + dp[N][3][2]) % 10000)
