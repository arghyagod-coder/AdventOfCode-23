with open('input.txt', 'r') as f:
    data= f.readlines()

sum = 0 

def get_game_data(s: str):
    s = s.replace(";", "")
    s = s.replace(",", "")
    elements = s.split()
    game_id= elements[1].replace(":", "")
    return int(game_id), elements[1:]

def return_max_values(elements: list):
    blue_values = []
    green_values = []
    red_values = []
    
    for index, element in enumerate(elements):
        if element == "blue":
            blue_values.append(int(elements[index-1]))
        elif element == "green":
            green_values.append(int(elements[index-1]))
        elif element == "red":
            red_values.append(int(elements[index-1]))

    blue_values.sort()
    red_values.sort()
    green_values.sort()

    return {
        "blue": blue_values[-1],
        "red": red_values[-1],
        "green": green_values[-1]
    }


for line in data:
    game_id, outcomes = get_game_data(line)
    values = return_max_values(outcomes)
    power = values["blue"] * values["red"] * values["green"]
    sum += power
    # print(f"Game {game_id}: {values}\nPower: {power}")

print(sum)
