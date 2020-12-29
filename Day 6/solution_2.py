import re
INPUT = open("./input.txt", "r")

groups = [group.splitlines() for group in INPUT.read().split("\n\n")]
flatten = lambda z: [x for y in z for x in y]

group_sums = 0

for group in groups:
	num_people = len(group)

	answers = flatten(group)
	answers_str = str(answers)

	group_question_count = 0

	for answer in set(answers):
		if answers_str.count(answer) == num_people:
			group_question_count += 1

	group_sums += group_question_count

print(group_sums)