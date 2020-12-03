import re

INPUT = open("./input", "r")
passwords = INPUT.readlines()
password_pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
valid_passwords_sum = 0

for password_entry in passwords:
	match = password_pattern.search(password_entry)

	pos1 = int(match.group(1)) - 1
	pos2 = int(match.group(2)) - 1
	letter = match.group(3)
	password = match.group(4)

	letter_pos1 = password[pos1]
	letter_pos2 = password[pos2]

	if (letter_pos1 == letter) ^ (letter_pos2 == letter):
		valid_passwords_sum += 1

print(valid_passwords_sum)