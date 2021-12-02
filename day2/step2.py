with open("input.txt") as f_in:
    lines_split = (s.split() for s in f_in.readlines())
    x_pos = 0
    y_pos = 0
    aim = 0
    for line in lines_split:
        if line[0] == "forward":
            x_pos += int(line[1])
            y_pos += int(line[1]) * aim
        elif line[0] == "down":
            aim += int(line[1])
        else:
            aim -= int(line[1])

    print(x_pos * y_pos)
