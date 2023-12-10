# Import regular expressions module
import re

# Define constants for the maximum number of each color
MAX_RED = 12  
MAX_GREEN = 13
MAX_BLUE = 14

# Define a function to extract the number of balls from a string
def extract_number(string):
    numbers_only = re.sub(r'\D', '', string)
    return int(numbers_only)

# Define a function to check if a game is valid
def is_valid_game(game):
    colors = game.split(",")
    
    for color in colors:
        number = extract_number(color)
        
        if "red" in color and number > MAX_RED:
            return False
        if "green" in color and number > MAX_GREEN:
            return False
        if "blue" in color and number > MAX_BLUE:
            return False
        
    return True

# Calculate result from input file 
def calculate_result(input_file):
    result = 0
    
    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            game_id, game_stats = line.split(":")
            game_id = extract_number(game_id)
            game_stats = game_stats.split(";")
            
            for game in game_stats:
                if not is_valid_game(game):
                    game_id = 0
                    break
                    
            result += game_id
            
    return result

# Print result
result = calculate_result("input.txt")
print(result)
