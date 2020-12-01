input_file = open("input.txt")
lines = input_file.readlines()
for line in lines:
    line = line.strip()
    for line_1 in lines:
        line_1 = line_1.strip()
        for line_2 in lines:
            if (int(line) + int(line_1) + int(line_2)) == 2020:
                print(str(int(line) * int(line_1) * int(line_2)))
