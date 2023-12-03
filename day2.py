#  12 red cubes, 13 green cubes, and 14 blue cubes
from collections import defaultdict
from functools import reduce

# rules = {"blue": 14, "red": 12, "green":13}
with open('day2.txt') as file:
    valid_games_power = 0
    for game in file:
        counts = {"blue": 0, "red": 0, "green": 0}
        game_id = game.split(':')[0].split(' ')[-1]
        cubes = game.strip().split(':')[1]
        for pick in cubes.split(';'):
            for count_and_colour in pick.split(','):
                _, count, colour = count_and_colour.split(' ')
                if int(count) >= counts[colour]:
                    counts[colour] = int(count)
        powers = reduce(lambda x, y : x*y, counts.values())
        valid_games_power += powers

print(valid_games_power)