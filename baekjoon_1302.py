import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
book = defaultdict(int)

for _ in range(n):
    book[input().strip()] += 1

booklist = sorted(book.items(), key=lambda x: x[0])
booklist = sorted(booklist, key=lambda x: x[1], reverse=True)
print(booklist[0][0])
