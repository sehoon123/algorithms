import sys
input = sys.stdin.readline

T = int(input())

for i in range(1,T+1):
    arr = list(map(int,input().split()))
    n = arr[0]
    arr = arr[1:]
    arr.sort()
    temp = 0
    for j in range(n-1):
        if arr[j+1]-arr[j] > temp:
            temp = arr[j+1]-arr[j]

    print(f'Class {i}')
    print(f'Max {arr[-1]}, Min {arr[0]}, Largest gap {temp}')
