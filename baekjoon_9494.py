import sys
import re
input = sys.stdin.readline


while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in range(n):
        s = input().rstrip()
        if (cnt > len(s)):
            continue
        for j in s[cnt:]:
            if j == ' ':
                break
            cnt += 1
    print(cnt + 1)





