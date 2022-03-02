n = int(input())
player = list(map(int,input().split()))

result = []

while len(player) > 1:
    idx = player.index(max(player))
    if idx == 0:
        result.append(player[0]-player[1])
        player.pop(idx)
    elif idx == len(player)-1:
        result.append(player[len(player)-1]-player[len(player)-2])
        player.pop(idx)
    else:
        result.append(player[idx]-max(player[idx-1],player[idx+1]))
        player.pop(idx)

print(sum(result))