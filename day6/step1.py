import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"

with open(f_in_name) as f_in:
    prev = list(map(lambda x: int(x), f_in.readline().split(",")))
    for i in range(80):
        new_list = [(x - 1) % 7 if x < 7 else x - 1 for x in prev]
        new_list += [8 for x in prev if x == 0]
        prev = new_list
    print(len(new_list))
