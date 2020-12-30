import re

INPUT = open("./input.txt", "r")

rules = INPUT.readlines()
bags_colors = set()
bags_colors.add("shiny gold")

while True:

	new_bags_color = bags_colors.copy()

	for bag_color in bags_colors:
		rule_pattern = re.compile(r"(\w+ \w+) bags .*? {}".format(bag_color))

		for rule in rules:
			if rule_pattern.match(rule):
				match_group = rule_pattern.search(rule)
				new_bags_color.add(match_group[1])

	if bags_colors == new_bags_color:
		break

	bags_colors = new_bags_color

print(len(bags_colors) - 1)