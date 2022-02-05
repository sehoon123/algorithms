import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X = int(''.join(input().split()))
    Y = int(''.join(input().split()))

    rullet = input().split()
    rullet = rullet * 2

    count = 0
    for i in range(N):
        tmp = int(''.join(rullet[i:i+M]))
        if X <= tmp <= Y:
            count += 1

    print(count)