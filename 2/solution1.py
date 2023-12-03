f = open("input.txt")
games = {}
max_red = 12
max_green = 13
max_blue = 14
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
	if colors['red'] <= max_red and colors['green'] <= max_green and colors['blue'] <= max_blue:
		total += game_id
print(total)
