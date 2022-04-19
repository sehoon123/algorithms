import sys
input = sys.stdin.readline

n = input().strip()

dec = int(n, 2)
result = oct(dec)
print(result[2:])
