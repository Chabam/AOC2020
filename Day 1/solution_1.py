import functools, itertools, operator

INPUT = open("./input.txt", "r")

entries = [int(num) for num in INPUT.readlines()]
entries_paired = itertools.combinations(entries, 2)
matching_entries = list(filter(lambda pair: pair[0] + pair[1] == 2020, entries_paired))[0]

print(functools.reduce(operator.mul, matching_entries))