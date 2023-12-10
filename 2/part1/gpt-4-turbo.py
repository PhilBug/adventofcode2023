import re

# Constants to represent the threshold for each color
NUMBER_OF_RED = 12
NUMBER_OF_GREEN = 13
NUMBER_OF_BLUE = 14

# Function to extract numbers from a string using regular expressions
def extract_numbers(string):
    numbers_only = re.sub(r'\D', '', string)
    return int(numbers_only)

# Function to process each color in the game statistics
def process_color_statistics(game_statistics):
    color_counters = {"red": 0, "green": 0, "blue": 0}

    # Split each game statistic and extract the color count
    for stat in game_statistics:
        colors = stat.split(",")
        for color in colors:
            color_number = extract_numbers(color)
            if "red" in color and color_number <= NUMBER_OF_RED:
                color_counters["red"] += color_number
            elif "green" in color and color_number <= NUMBER_OF_GREEN:
                color_counters["green"] += color_number
            elif "blue" in color and color_number <= NUMBER_OF_BLUE:
                color_counters["blue"] += color_number

    return not (color_counters["red"] > NUMBER_OF_RED or \
                color_counters["green"] > NUMBER_OF_GREEN or \
                color_counters["blue"] > NUMBER_OF_BLUE)

# Function to process the input file and calculate the result
def process_games(input_file_path):
    result = 0
    with open(input_file_path, "r") as input_file:
        lines = [line.strip() for line in input_file]
        
        for game in lines:
            game_id, game_statistics = game.split(":")
            game_id = int(game_id.split(" ")[1])
            game_statistics = game_statistics.split(";")
            
            if process_color_statistics(game_statistics):
                result += game_id

    return result

# Calling the main processing function and printing the result
if __name__ == "__main__":
    result = process_games("input.txt")
    print(result)