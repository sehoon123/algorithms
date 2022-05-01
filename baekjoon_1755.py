import sys
input = sys.stdin.readline

dictionary = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "10":"ten"}

temp ={}

n, m = map(int, input().split())

for i in range(n, m+1):
    result = ""
    for j in list(str(i)):
        result += dictionary[j]
    temp[str(i)] = result

# print(temp)

res = dict((v,k) for k,v in temp.items())
res_list = list(res.keys())
res_list.sort()
# print(res_list)

for i in range(0, len(res_list)):
    if i % 10 == 0 and i != 0:
        print()
    print(res[res_list[i]], end=" ")