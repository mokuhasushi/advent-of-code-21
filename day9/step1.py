import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"


def check_mask(field, i, j):
    value = field[i][j]
    if i != 0:
        if field[i - 1][j] < value:
            return False
    if i != len(field) - 1:
        if field[i + 1][j] < value:
            return False
    if j != 0:
        if field[i][j - 1] < value:
            return False
    if j != len(field[0]) - 1:
        if field[i][j + 1] < value:
            return False
    return True


with open(f_in_name) as f_in:
    field = f_in.readlines()
    field = list(map(lambda s: s.strip(), field))
    field = [[int(x) for x in line] for line in field]

    lowpoints = []
    sum = 0

    for i in range(len(field)):
        for j in range(len(field[0])):
            if check_mask(field, i, j):
                lowpoints.append((i, j))
                sum += 1 + field[i][j]

    print(sum, lowpoints)
