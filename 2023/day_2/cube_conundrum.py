colors = {"red": 12, "blue": 14, "green": 13}
from collections import defaultdict


def solution(input):
    input = input.split("\n")
    games = []
    sum = 0
    for game in input:
        games.append(game_parser(game))

    for i, game in enumerate(games):
        product = 1
        max_counter = defaultdict()
        for cube in game:
            for color in colors:
                if color in cube:
                    if int(cube[color]) > max_counter.get(color, 0):
                        max_counter[color] = int(cube[color])

        for colr in max_counter:
            product *= max_counter[colr]
        sum += product
    return sum


# def solution(input):
#     input = input.split("\n")
#     games = []
#     possible_game_ids_sum = 0
#     for game in input:
#         games.append(game_parser(game))

#     for i, game in enumerate(games):
#         is_possible = True
#         for cube in game:
#             for color in colors:
#                 if color in cube:
#                     if is_impossible_game(color, cube):
#                         is_possible = False
#         if is_possible:
#             possible_game_ids_sum += i + 1

#     return possible_game_ids_sum


def is_impossible_game(color, cube):
    return int(cube[color]) > colors[color]


def game_parser(game):
    parsed_sets = []
    sets = game[8:].strip().split(";")
    for set in sets:
        cubes = set.strip().split(",")
        for cube in cubes:
            cube = cube.strip().split(" ")
            parsed_sets.append({cube[1]: cube[0]})

    return parsed_sets
