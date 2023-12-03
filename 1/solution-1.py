f = open("input.txt")
total = 0
for line in f:
	first_digit = None
	last_digit = None
	if not line.strip():
		continue
	for char in line.strip():
		if not char.isdigit():
			continue
		if first_digit is None:
			first_digit = char
		last_digit = char
	total += int(first_digit + last_digit)

print(total)
