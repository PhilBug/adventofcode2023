import re

NUMBER_OF_RED = 12
NUMBER_OF_GREEN = 13
NUMBER_OF_BLUE = 14

def extract_numbers(string):
    numbers_only = re.sub(r'\D', '', string)
    return int(numbers_only)

def process_game(game):
    game_id = int(game.split(":")[0].split(" ")[1])
    game_statistics = game.split(":")[1].split(";")

    for stat in game_statistics:
        stats = stat.split(",")
        for color_data in stats:
            color, number = color_data.split()
            color_number = extract_numbers(number)

            if color == "red" and color_number > NUMBER_OF_RED:
                game_id = 0
            elif color == "green" and color_number > NUMBER_OF_GREEN:
                game_id = 0
            elif color == "blue" and color_number > NUMBER_OF_BLUE:
                game_id = 0

    return game_id

def calculate_result(lines):
    result = 0
    for game in lines:
        game_id = process_game(game)
        result += game_id

    return result

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file]
    result = calculate_result(lines)
    print(result)