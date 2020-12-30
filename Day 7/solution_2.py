import re

INPUT = open("./input.txt", "r")

rules = INPUT.readlines()

class BagGraph:
	def __init__(self, color, count):
		self.color = color
		self.count = count
		self.childs = []

	def add_child(self, bag_graph):
		if type(bag_graph) is not BagGraph:
			raise ValueError("Childs must be BagGraphs!")

		self.childs.append(bag_graph)

	def count_total(self):
		if not self.childs:
			return self.count

		sub_total = 0
		for bag_graph in self.childs:
			sub_total += bag_graph.count_total()

		return self.count + self.count * sub_total

	def print(self, spacing=0):
		print("{}{} * {}".format("\t" * spacing, self.count, self.color))
		for child in self.childs:
			child.print(spacing + 1)


root = BagGraph("!!!temp root!!!", 0)
root.add_child(BagGraph("shiny gold", 1))

sub_color_pattern = re.compile(r"(\d+) (\w+ \w+) bag")

def build_bag_graph(bag_graph):
	for child in bag_graph.childs:

		rule_with_color = list(filter(lambda rule: rule.startswith(child.color), rules))[0]
		color_pattern = re.compile(r"^{} bags contain (\d+.*)".format(child.color))
		match_group = color_pattern.search(rule_with_color)
		if match_group is None:
			continue

		child_bags = match_group[1].split(", ")

		for child_bag in child_bags:
			match_group = sub_color_pattern.search(child_bag)
			count = int(match_group[1])
			sub_color = match_group[2]

			child.add_child(BagGraph(sub_color, count))

		build_bag_graph(child)

build_bag_graph(root)
shiny_gold_bag = root.childs[0]
shiny_gold_bag.print()

# -1 because we don't count the shiny gold bag itself
print(shiny_gold_bag.count_total() - 1)