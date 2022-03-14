import sys
input = sys.stdin.readline


n = int(input())
home = [0] * (n//2)
away = [0] * (n//2)

cards = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        if i == 0:
            home[0] = cards[i]
        else:
            home[i//2] = home[i//2 -1] + cards[i]
    else:
        if i == 1:
            away[0] = cards[i]
        else:
            away[i//2] = away[i//2 - 1] + cards[i]

MAX = home[-1]
home = [0] + home
away = [0] + away
for i in range(n//2+1):
    MAX = max(MAX, home[i] + away[-1] - away[i], home[i] + away[-2] - away[i-1])

print(MAX)