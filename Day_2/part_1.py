with open('input.txt', 'r') as f:
    data= f.readlines()


max_blue = 14
max_green = 13
max_red = 12

sum = 0 

def get_game_data(s: str):
    s = s.replace(";", "")
    s = s.replace(",", "")
    elements = s.split()
    game_id= elements[1].replace(":", "")
    return int(game_id), elements[1:]

def check_possibility(elements: list):
    for index, element in enumerate(elements):
        if element == "blue":
            if int(elements[index-1])>max_blue:
                return False
                break 
            else:
                continue
        elif element == "green":
            if int(elements[index-1])>max_green:
                return False
                break
            else:
                continue
        elif element == "red":
            if int(elements[index-1])>max_red:
                return False
                break 
            else:
                continue

for line in data:
    game_id, outcomes = get_game_data(line)
    possible = check_possibility(outcomes)
    if possible==False:
        continue
    else:
        sum += game_id

print(sum)

    

        
