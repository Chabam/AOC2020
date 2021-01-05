INPUT = open("./input.txt", "r")

jolts = sorted([int(jolt) for jolt in INPUT.readlines()])
jolts.append(jolts[-1] + 3)
jolts = [0] + jolts

jolt_diffs = {}
for start_idx in range(1, len(jolts)):
	jolt_diff = jolts[start_idx] - jolts[start_idx - 1]

	if jolt_diff not in jolt_diffs:
		jolt_diffs[jolt_diff] = 0

	jolt_diffs[jolt_diff] += 1

print(jolt_diffs[1] * jolt_diffs[3])