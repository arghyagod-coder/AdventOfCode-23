with open('input.txt', 'r') as f:
    data = f.readlines()

sum = 0

for line in data:
    # print(f"Line {data.index(line)}:  "+ line)

    numerics = []
    
    for i in line:
        if i.isdigit():
            numerics.append(int(i))

    if len(numerics)==1:
        # print(int(str(numerics[0]) + str(numerics[-1])))
        sum += int(str(numerics[0]) + str(numerics[0]))
    else:
        # print(int(str(numerics[0]) + str(numerics[-1])))
        sum += int(str(numerics[0]) + str(numerics[-1]))
    
    # print(sum)

print(sum)