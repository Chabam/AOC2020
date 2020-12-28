import functools, operator

INPUT = open("./input.txt", "r")

tree_map = [list(line.rstrip()) for line in INPUT.readlines()]
slope_configurations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = []

for slope_configuration in slope_configurations:
	tree_count = 0
	print("*" * 100)
	for line_idx in range(len(tree_map)):
		x_slope, y_slope = slope_configuration
		y = line_idx * y_slope

		if y > len(tree_map):
			break

		line = tree_map[y]

		x = (line_idx * x_slope) % (len(line))

		if line[x] == "#":
			tree_count += 1

	tree_counts.append(tree_count)

print(tree_counts)
print(int(functools.reduce(operator.mul, tree_counts)))