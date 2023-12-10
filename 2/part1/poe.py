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
    print(f"game_id: {game_id}, game_statistics: {game_statistics}")

    for game_stat in game_statistics:
        colors = game_stat.split(",")
        print(colors)
        for color in colors:
            if "red" in color:
                color_number = extract_numbers(color)
                if color_number > NUMBER_OF_RED:
                    game_id = 0
            if "green" in color:
                color_number = extract_numbers(color)
                if color_number > NUMBER_OF_GREEN:
                    game_id = 0
            if "blue" in color:
                color_number = extract_numbers(color)
                if color_number > NUMBER_OF_BLUE:
                    game_id = 0
    return game_id

def calculate_result():
    result = 0
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
        for game in lines:
            game_id = process_game(game)
            result += game_id
    return result

print(calculate_result())