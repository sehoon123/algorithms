import math
import sys
input = sys.stdin.readline

nums = [1 for _ in range(10000001)]
nums[0] = 0
nums[1] = 0

for i in range(2, int(math.sqrt(10000001)) + 1):
    if nums[i] == 0:
        continue
    for j in range(i * 2, 10000001, i):
        nums[j] = 0


while True:
    n = int(input())
    if n == 0:
        break

    for i in range(3, n + 1):
        if nums[i] == 1 and nums[n - i] == 1:
            print(f'{n} = {i} + {n - i}')
            break
    else:
        print('Goldbach\'s conjecture is wrong.')

