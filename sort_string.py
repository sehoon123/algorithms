# string = input()
string = "AJKDLSI412K4JSJ9D"
for s in string:
    print(s)
char_list = [string[i] for i in range(len(string))]
char_list.sort()

result = 0
count = 0
for i in char_list:
    try:
        result += int(i)
        count += 1
        char_list.remove(char_list[i])
    except :
        continue

print("".join(char_list[count:])+str(result))
