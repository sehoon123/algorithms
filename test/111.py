import sys
input = sys.stdin.readline

n = input().strip()

dec = int(n, 8)
result = bin(dec)[2:]
print(result)
