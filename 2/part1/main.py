# example input.txt:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
import re

NUMBER_OF_RED=12
NUMBER_OF_GREEN=13
NUMBER_OF_BLUE=14

def extract_numbers(string):
    numbers_only = re.sub(r'\D', '', string)
    return int(numbers_only)

result = 0
with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file]
    for game in lines:
        game_id = int(game.split(":")[0].split(" ")[1])
        game_statistics = game.split(":")[1].split(";")
        print(f"game_id: {game_id}, game_statistics: {game_statistics}")

        for game in game_statistics:
            game = game.split(",")
            print(game)
            for color in game:
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
        result += game_id
    print(result)