import itertools

INPUT = open("./input.txt", "r")

numbers = [int(num) for num in INPUT.readlines()]
preamble_size = 25
corrupted_number = None

for number_idx in range(preamble_size, len(numbers)):
	number = numbers[number_idx]
	preamble = numbers[number_idx - preamble_size:number_idx]

	possible_sums = list(map(lambda pair: pair[0] + pair[1], itertools.combinations(preamble, 2)))

	if number not in possible_sums:
		corrupted_number = number
		break

start_idx = 0
end_idx = start_idx + 1
contiguous_set = None
contiguous_sum = 0

while contiguous_sum != corrupted_number:

	contiguous_set = numbers[start_idx:end_idx]
	contiguous_sum = sum(contiguous_set)
	if corrupted_number < contiguous_sum:
		start_idx += 1
		end_idx = start_idx + 1
		continue

	end_idx += 1

print(contiguous_set, max(contiguous_set) + min(contiguous_set))