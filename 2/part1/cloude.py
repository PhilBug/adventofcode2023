import re

NUMBER_OF_RED = 12
NUMBER_OF_GREEN = 13 
NUMBER_OF_BLUE = 14

def extract_numbers(string):
  numbers_only = re.sub(r'\D', '', string)
  return int(numbers_only)

def parse_game(game_string):
  game_id, game_stats = game_string.split(":") 
  game_id = int(game_id.split()[1])
  game_stats = game_stats.split(";")
  return game_id, game_stats

def validate_colors(colors):
  for color in colors:
    number = extract_numbers(color)
    if "red" in color and number > NUMBER_OF_RED:
      return 0
    if "green" in color and number > NUMBER_OF_GREEN:  
      return 0
    if "blue" in color and number > NUMBER_OF_BLUE:
      return 0
  return 1

def process_game(game_string):
  game_id, game_stats = parse_game(game_string)
  score = game_id
  for stats in game_stats:
    colors = stats.split(",")
    score *= validate_colors(colors)
  return score

def run():
  score = 0
  with open("input.txt") as f:
    for line in f:  
      score += process_game(line)
  return score

print(run())