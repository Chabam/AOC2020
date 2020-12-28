INPUT = open("./input.txt", "r")

tree_map = [list(line) for line in INPUT.readlines()]
tree_count = 0
for y in range(len(tree_map)):
	line = tree_map[y]
	x = (y * 3) % (len(line) - 1)
	if line[x] == "#":
		tree_count += 1

print(tree_count)