k, n = map(int, input().split())
values = [int(input()) for _ in range(k)]

start = 1
end = max(values)

# while start <= end:
#     mid = (start + end) // 2
#     count = 0
#     for value in values:
#         count += value // mid
#     if count >= n:
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(start - 1)

while start <= end :
    mid = (start + end) // 2
    count = 0
    for value in values:
        count += value // mid
        if