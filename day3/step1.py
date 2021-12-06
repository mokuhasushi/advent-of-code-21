# with open("sample.txt") as f_in:
with open("input.txt") as f_in:
    first_line = f_in.readline()
    input_len = len(first_line) - 1
    ones = [0] * input_len
    zeros = [0] * input_len
    for i in range(input_len):
        if first_line[i] == "0":
            zeros[i] += 1
        elif first_line[i] == "1":
            ones[i] += 1

    for line in f_in.readlines():
        for i in range(input_len):
            if line[i] == "0":
                zeros[i] += 1
            elif line[i] == "1":
                ones[i] += 1

    gamma_rate = ""
    epsilon_rate = ""

    for i in range(input_len):
        if zeros[i] > ones[i]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    gamma_n = int(gamma_rate, 2)
    epsilon_n = int(epsilon_rate, 2)
    print(gamma_n * epsilon_n)
