import re

NUMBER_OF_RED = 12
NUMBER_OF_GREEN = 13
NUMBER_OF_BLUE = 14

def main():
    result = 0
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
        for game in lines:
            game_id, game_statistics = parse_game_data(game)
            game_id = process_game_statistics(game_id, game_statistics)
            result += game_id
        print(result)

def parse_game_data(game):
    game_id = int(game.split(":")[0].split(" ")[1])
    game_statistics = game.split(":")[1].split(";")
    return game_id, game_statistics

def process_game_statistics(game_id, game_statistics):
    for game in game_statistics:
        game = game.split(",")
        for color in game:
            game_id = validate_color(color, game_id)
    return game_id

def extract_numbers(string):
    numbers_only = re.sub(r'\D', '', string)
    return int(numbers_only)

def validate_color(color, game_id):
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

if __name__ == "__main__":
    main()