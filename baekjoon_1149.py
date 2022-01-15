n = int(input())
house = [[] for _ in range(n)]

for i in range(n):
    house[i] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(3):
        if j == 0:
            tmp = min(house[i-1][1], house[i-1][2])
        elif j == 1:
            tmp = min(house[i-1][0], house[i-1][2])
        else:
            tmp = min(house[i-1][0], house[i-1][1])

        house[i][j] = house[i][j] + tmp
print(min(house[n-1]))