#49 13 :39 46 58 73
import sys
from collections import defaultdict

input = sys.stdin.readline

trees = defaultdict(int)

count = 0
while True:
    tree = input().strip()
    if tree == "":
        break
    trees[tree] += 1
    count += 1

new_trees = sorted(trees.items())

for i in range(len(new_trees)):
    print(f'{new_trees[i][0]} {100 * new_trees[i][1] / count:.4f}')


