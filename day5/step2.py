import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"


def process_line(line):
    tup = line.split("->")
    start = tup[0].split(",")
    end = tup[1].split(",")
    return (int(start[0]), int(start[1])), (int(end[0]), int(end[1]))


with open(f_in_name) as f_in:
    field = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in f_in.readlines():
        start, finish = process_line(line)
        # print(start, finish)
        if start[0] == finish[0]:
            if start[1] > finish[1]:
                tmp = start
                start = finish
                finish = tmp
            for i in range(start[1], finish[1] + 1):
                field[i][start[0]] += 1
        elif start[1] == finish[1]:
            if start[0] > finish[0]:
                tmp = start
                start = finish
                finish = tmp
            for i in range(start[0], finish[0] + 1):
                field[start[1]][i] += 1
        else:
            if start[0] > finish[0]:
                tmp = start
                start = finish
                finish = tmp
            if start[1] < finish[1]:
                for i, j in zip(
                    range(start[0], finish[0] + 1), range(start[1], finish[1] + 1)
                ):
                    field[j][i] += 1
            else:
                for i, j in zip(
                    range(start[0], finish[0] + 1), range(start[1], finish[1] - 1, -1)
                ):
                    field[j][i] += 1

    final = [item for row in field for item in row if item > 1]
    print(len(final))
