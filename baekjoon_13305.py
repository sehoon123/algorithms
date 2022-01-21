n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

total = 0
cheap = 1000000001
for i in range(n-1):
    if price[i] < cheap:
        cheap = price[i]
    total += distance[i] * cheap

print(total)
