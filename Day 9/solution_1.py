import itertools

INPUT = open("./input.txt", "r")

numbers = [int(num) for num in INPUT.readlines()]
preamble_size = 25

for number_idx in range(preamble_size, len(numbers)):
	number = numbers[number_idx]
	preamble = numbers[number_idx - preamble_size:number_idx]

	possible_sums = list(map(lambda pair: pair[0] + pair[1], itertools.combinations(preamble, 2)))

	if number not in possible_sums:
		print(number)
		break
