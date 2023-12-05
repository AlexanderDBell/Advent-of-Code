import re

with open('day_2\input.txt') as f:
    input = f.read()

def find_colour(query, string):
    colour = re.findall(query, string)
    if colour == []:
        return 0
    return int(colour[0])

def sum_id(data):
    games = data.split('\n')
    query = r'(?<=: ).*'
    games = [re.findall(query, game)[0] for game in games]
    games = [game.split('; ') for game in games]
    game_results = []
    for game in games:
        red_number_list = []
        green_number_list = []
        blue_number_list = []
        for round in game:
            red_query = r'\d+(?= r)'
            green_query = r'\d+(?= g)'
            blue_query = r'\d+(?= b)'
            red_number = find_colour(red_query, round)
            green_number = find_colour(green_query, round)
            blue_number = find_colour(blue_query, round)
            red_number_list.append(red_number)
            green_number_list.append(green_number)
            blue_number_list.append(blue_number)
        max_red = max(red_number_list)
        max_green = max(green_number_list)
        max_blue = max(blue_number_list)
        game_results.append(max_red*max_green*max_blue)
    return sum(game_results)

print(sum_id(input))