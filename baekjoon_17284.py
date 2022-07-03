price = {1:500, 2:800, 3:1000}
initial = 5000
push = list(map(int, input().split()))

for i in push:
    initial -= price[i]

print(initial)
