import functools

INPUT = open("./input.txt", "r")

jolts = sorted([int(jolt) for jolt in INPUT.readlines()])
jolts.append(jolts[-1] + 3)
jolts = [0] + jolts
num_adapter_sequences = 0

@functools.lru_cache
def build_adpater_sequence(current_idx):
	if current_idx == len(jolts) - 1:
		return 1

	last_number = jolts[current_idx]

	total = 0
	for idx in range(current_idx + 1, len(jolts)):
		if jolts[idx] - last_number > 3:
			break

		total += build_adpater_sequence(idx)

	return total

print(build_adpater_sequence(0))