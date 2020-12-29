import re
INPUT = open("./input.txt", "r")

passports = INPUT.read().split("\n\n")
required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

total_valid_passport = 0
for passport in passports:
	all_field_present = True

	for field in required_fields:
		if field not in passport:
			all_field_present = False
			break

	if all_field_present:
		total_valid_passport += 1

print(total_valid_passport)