A,B,C = map(int, input().split())
def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i*B
    for j in range(n+1):
        dp[0][j] = j*B
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+A
            else:
                dp[i][j] = max(dp[i-1][j]+B, dp[i][j-1]+B, dp[i-1][j-1]+C)
    return dp[m][n]

print(edit_distance(input(), input()))