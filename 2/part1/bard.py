import re

NUMBER_OF_RED = 12
NUMBER_OF_GREEN = 13
NUMBER_OF_BLUE = 14

def parse_game_data(game_data):
    game_id = int(game_data.split(":")[0].split(" ")[1])
    game_statistics = game_data.split(":")[1].split(";")
    filtered_statistics = []

    for stat in game_statistics:
        stats = stat.split(",")
        filtered_stats = []

        for color_data in stats:
            color, number = color_data.split()
            color_number = int(number)

            if color == "red" and color_number > NUMBER_OF_RED:
                game_id = 0
                break
            elif color == "green" and color_number > NUMBER_OF_GREEN:
                game_id = 0
                break
            elif color == "blue" and color_number > NUMBER_OF_BLUE:
                game_id = 0
                break
            else:
                filtered_stats.append((color, color_number))

        if game_id == 0:
            break

        filtered_statistics.append(", ".join(["{} {}".format(color, number) for color, number in filtered_stats]))

    return game_id, "; ".join(filtered_statistics)

result = 0
with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file]

    for game in lines:
        game_id, game_data = parse_game_data(game)
        if game_id:
            result += game_id

    print(result)