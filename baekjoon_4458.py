import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    temp = input().rstrip()
    print(temp[0].upper() + temp[1:])

