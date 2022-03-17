import sys
input = sys.stdin.readline

string = input().rstrip()
string = list(string)
string.sort()
string = "".join(string)
print(string)