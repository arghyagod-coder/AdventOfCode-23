with open('input.txt', 'r') as f:
    data = f.readlines()

wordnums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0

for line in data:
    # print(f"Line {data.index(line)}:  "+ line)
    s = ""
    
    numerics = []
    
    for i in line:
        if i.isdigit():
            numerics.append(int(i))
            s = ""
        else:
            s += i
            for num in wordnums: 
                if num in s:
                    numerics.append(wordnums.index(num))
                    s = ""
    
    if len(numerics)==1:
        # print(int(str(numerics[0]) + str(numerics[-1])))
        sum += int(str(numerics[0]) + str(numerics[0]))
    else:
        # print(int(str(numerics[0]) + str(numerics[-1])))
        sum += int(str(numerics[0]) + str(numerics[-1]))
    
    # print(sum)

print(sum)