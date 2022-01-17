n = int(input())

score = []
d = [0 for i in range(301)]
for i in range(n):
    score.append(int(input()))
d[0] = score[0]
d[1] = score[0]+score[1]
d[2] = max(score[0]+score[2], score[1]+score[2])

for i in range(3, n):
    d[i] = max(d[i-3] + score[i-1] + score[i], d[i-2] + score[i])

print(d[n-1])
