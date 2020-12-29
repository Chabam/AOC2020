import re
INPUT = open("./input.txt", "r")

passports = INPUT.read().split("\n\n")
required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
height_pattern = re.compile(r"^(\d+)(in|cm)$")
hair_color_pattern = re.compile(r"^#[a-f0-9]{6}$")
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
passport_id_pattern = re.compile(r"^[0-9]{9}$")
flatten = lambda z: [x for y in z for x in y]

total_valid_passport = 0
for passport in passports:
	all_field_present = True
	field_values = [field.split() for field in passport.split("\n")]
	field_values = flatten(field_values)

	field_dict = {}
	for field in field_values:
		field_name, field_value = field.split(":")
		field_dict[field_name] = field_value

	for field in required_fields:
		if field not in passport:
			all_field_present = False
			break

	if not all_field_present:
		continue

	all_field_valid = True
	for field_name, field_value in field_dict.items():
		if "byr" == field_name and int(field_value) in range(1920, 2003):
			continue
		elif "iyr" == field_name and int(field_value) in range(2010, 2021):
			continue
		elif "eyr" == field_name and int(field_value) in range(2020, 2031):
			continue
		elif "hgt" == field_name and height_pattern.match(field_value):
			match_group = height_pattern.search(field_value)

			if ((match_group[2] == "cm" and int(match_group[1]) in range(150, 194)) or
				(match_group[2] == "in" and int(match_group[1]) in range(59, 77))):
				continue
		elif "hcl" == field_name and hair_color_pattern.match(field_value):
			continue
		elif "ecl" == field_name and field_value in eye_colors:
			continue
		elif "pid" == field_name and passport_id_pattern.match(field_value):
			continue
		elif "cid" == field_name:
			continue

		all_field_valid = False
		break

	if all_field_valid:
		total_valid_passport += 1

print(total_valid_passport)