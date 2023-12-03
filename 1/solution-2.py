f = open("input.txt")
total = 0

words = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9"
}

for line in f:
	first_digit = None
	last_digit = None
	digit = None
	if not line.strip():
		continue
	for i in range(len(line)):
		if line[i].isdigit():
			digit = line[i]
		else:
			for word in words:
				if line[i:i+len(word)] == word:
					digit = words[word]
					i = i + len(word)
					break
		if first_digit is None:
			first_digit = digit
		last_digit = digit
	print(int(first_digit + last_digit))
	total += int(first_digit + last_digit)

print(total)
