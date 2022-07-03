import sys

input = sys.stdin.readline

n = int(input())

player = []
country = [0] * (n+1)

medal = []

for _ in range(n):
    player.append(list(map(int, input().split())))

player.sort(key=lambda x: x[2], reverse=True)


for i in range(n):
    if country[player[i][0]] < 2:
        country[player[i][0]] += 1
        medal.append(player[i])

    if len(medal) == 3:
        break

print(*medal[0][:2])
print(*medal[1][:2])
print(*medal[2][:2])