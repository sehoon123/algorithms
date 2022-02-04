n, m = map(int, input().split())
limit = []
velocity = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a):
        limit.append(b)

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a):
        velocity.append(b)

max = 0
for i in range(len(limit)):
    if velocity[i] - limit[i] > max:
        max = velocity[i] - limit[i]

print(max)
