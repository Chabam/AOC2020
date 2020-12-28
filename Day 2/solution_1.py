import re

INPUT = open("./input.txt", "r")
passwords = INPUT.readlines()
password_pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
valid_passwords_sum = 0

for password_entry in passwords:
	match = password_pattern.search(password_entry)

	min = int(match.group(1))
	max = int(match.group(2))
	letter = match.group(3)
	password = match.group(4)

	count = password.count(letter)
	if min <= count and max >= count:
		valid_passwords_sum += 1

print(valid_passwords_sum)