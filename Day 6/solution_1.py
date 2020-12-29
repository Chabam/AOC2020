import re
INPUT = open("./input.txt", "r")

groups = INPUT.read().split("\n\n")
flatten = lambda z: [x for y in z for x in y]

print(sum([len(set(flatten(group.splitlines()))) for group in groups]))