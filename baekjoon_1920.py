# def binary_search(a, x):
#     start, end = 0, len(a) -1
#     while start <= end:
#         mid = (start + end) // 2
#         if a[mid] == x:
#             return mid
#         elif a[mid] > x:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1
#
# print(binary_search(a, 3))

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# for ele in B:
#     if A.__contains__(ele):
#         print(1)
#     else:
#         print(0)

for ele in B:
    if ele in A:
        print(1)
    else:
        print(0)