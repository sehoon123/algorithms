n = input()
a = list(n)
a.sort(reverse=True)
b = [int(i) for i in a]

result = b[0]
for i in range(1, len(b)):
    if b[i] == 0:
        continue
    if b[i] == 1:
        result += 1
    result *= b[i]

print(result)