f = open("input.txt")
games = {}
for line in f:
	if not line.strip():
		continue
	game, rocks = line.strip().split(": ")
	handfuls = rocks.split("; ")
	game_id = int(game[5:])
	games[game_id] = {"red": 0, "green": 0, "blue": 0}
	for handful in handfuls:
		by_color = handful.split(", ")
		for color_str in by_color:
			count, color = color_str.split(" ")
			games[game_id][color] = max(int(count), games[game_id][color])

total = 0
for game_id, colors in games.items():
	total += (colors['red'] * colors['green'] * colors['blue'])
print(total)
