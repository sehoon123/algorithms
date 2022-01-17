n = int(input())
score = [0] *  10001
d = [0] * 10001
for i in range(1,n+1):
    score[i] = int(input())

d[1] = score[1]
d[2] = score[1] + score[2]
d[3] = max(score[1] + score[3], score[2] + score[3], d[2])
for i in range(4, n+1):
    d[i] = max(d[i-1], score[i] + d[i-2], score[i] + score[i-1]+d[i-3])
print(max(d))