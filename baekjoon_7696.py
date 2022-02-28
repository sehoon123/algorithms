from collections import Counter, defaultdict
import array

i = 0
arr = array.array('i')
while len(arr) < 1000000:
    int_dict = defaultdict(int)
    i += 1
    flag = True
    for v in str(i):
        if int_dict[v]:
            flag = False
            break
        int_dict[v] += 1
    if flag:
        arr.append(i)



while True:
    n = input()
    if n == '0':
        break
    print(arr[int(n)-1])
