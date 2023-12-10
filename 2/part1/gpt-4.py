import re

NUMBER_OF_RED = 12
NUMBER_OF_GREEN = 13
NUMBER_OF_BLUE = 14


# Function to extract numbers from a string
def extract_numbers(string):
    numbers_only = re.sub(r"\D", "", string)
    return int(numbers_only)


# Function to process the color
def process_color(color, game_id, color_limit):
    color_number = extract_numbers(color)
    if color_number > color_limit:
        game_id = 0
    return game_id
def random_test_function():
    pass

# Function to process the game
def process_game(game_statistics):
    game_id = int(game_statistics.split(":")[0].split(" ")[1])
    rounds = game_statistics.split(":")[1].split(";")

    for round in rounds:
        colors = round.split(",")
        for color in colors:
            if "red" in color:
                game_id = process_color(color, game_id, NUMBER_OF_RED)
            elif "green" in color:
                game_id = process_color(color, game_id, NUMBER_OF_GREEN)
            elif "blue" in color:
                game_id = process_color(color, game_id, NUMBER_OF_BLUE)
    return game_id


# Main function to parse and process the file
def process_file(filename):
    result = 0
    with open(filename, "r") as input_file:
        lines = [line.strip() for line in input_file]
        for game_statistics in lines:
            result += process_game(game_statistics)
    print(result)


# Call the main function
process_file("input.txt")
