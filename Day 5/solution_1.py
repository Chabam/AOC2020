import re
INPUT = open("./input.txt", "r")

seats = INPUT.readlines()
rows = range(128)
cols = range(8)

def find_row(seat_seq, cur_rows):
	if len(cur_rows) == 1:
		return cur_rows[0]

	half_point = int(len(cur_rows) / 2)
	cur_letter, *rest = seat_seq
	if cur_letter == "B":
		return find_row(rest, cur_rows[half_point:])
	elif cur_letter == "F":
		return find_row(rest, cur_rows[:half_point])

def find_col(seat_seq, cur_cols):
	if len(cur_cols) == 1:
		return cur_cols[0]

	half_point = int(len(cur_cols) / 2)
	cur_letter, *rest = seat_seq
	if cur_letter == "R":
		return find_col(rest, cur_cols[half_point:])
	elif cur_letter == "L":
		return find_col(rest, cur_cols[:half_point])

seat_ids = []

for seat in seats:
	row = find_row(seat[:7], rows)
	col = find_col(seat[7:], cols)

	seat_ids.append(row * 8 + col)

print(max(seat_ids))