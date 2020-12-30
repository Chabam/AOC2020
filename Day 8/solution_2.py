import re

INPUT = open("./input.txt", "r")

original_instructions = INPUT.readlines()

def run_program(instructions):
	accumulator = 0
	cur_instruction_idx = 0
	ran_instructions = set()

	while cur_instruction_idx < len(instructions):
		ran_instructions.add(cur_instruction_idx)

		cur_instruction = instructions[cur_instruction_idx]

		action, value = cur_instruction.split(" ")
		value = int(value)

		next_instruction = cur_instruction_idx + 1
		if action == "acc":
			accumulator += value
		elif action == "jmp":
			next_instruction = cur_instruction_idx + value

		if next_instruction in ran_instructions:
			return None

		cur_instruction_idx = next_instruction

	return accumulator

for instruction_idx, instruction in enumerate(original_instructions):
	if instruction.startswith("acc"):
		continue

	new_instructions = original_instructions.copy()
	if instruction.startswith("nop"):
		new_instructions[instruction_idx] = instruction.replace("nop", "jmp")
	else:
		new_instructions[instruction_idx] = instruction.replace("jmp", "nop")

	res = run_program(new_instructions)
	if res is not None:
		print(res)
