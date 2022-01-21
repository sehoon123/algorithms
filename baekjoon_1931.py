n = int(input())
schedule = []
for i in range(n):
    start, end = map(int, input().split())
    schedule.append((start, end))

schedule.sort(key=lambda x: x[0])
schedule.sort(key=lambda x: x[1])

result = []
result.append(schedule[0])
for i in range(1,n):
    if schedule[i][0] >= result[-1][1]:
        result.append(schedule[i])

print(len(result))
