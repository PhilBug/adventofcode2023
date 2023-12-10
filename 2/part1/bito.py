import re
def read_input(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
    return lines
def parse_game(game_str):
    id = int(game_str.split(":")[0].split(" ")[1]) 
    stats = game_str.split(":")[1].split(";")
    return id, stats
def check_stats(stats, max_red, max_green, max_blue):
    for stat in stats:
        for color in stat.split(","):
            if "red" in color:
                num = extract_numbers(color) 
                if num > max_red:
                    return 0
            if "green" in color:
                num = extract_numbers(color)
                if num > max_green:
                    return 0
            if "blue" in color:
                num = extract_numbers(color)
                if num > max_blue:
                    return 0
    return 1
def extract_numbers(string):
    numbers_only = re.sub(r'\D', '', string)
    return int(numbers_only)
def calculate_score(lines):
    score = 0
    max_red = 12
    max_green = 13 
    max_blue = 14
    for line in lines:
        id, stats = parse_game(line)
        valid = check_stats(stats, max_red, max_green, max_blue)
        if valid:
            score += id
    return score
lines = read_input("input.txt")
score = calculate_score(lines)
print(score)