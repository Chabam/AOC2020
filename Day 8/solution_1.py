import re

INPUT = open("./input.txt", "r")

instructions = INPUT.readlines()
accumulator = 0
cur_instruction_idx = 0
ran_instructions = set()

while cur_instruction_idx not in ran_instructions:
	ran_instructions.add(cur_instruction_idx)

	cur_instruction = instructions[cur_instruction_idx]

	action, value = cur_instruction.split(" ")
	value = int(value)

	if action == "acc":
		accumulator += value
	elif action == "jmp":
		cur_instruction_idx += value
		continue

	cur_instruction_idx += 1


print(accumulator)