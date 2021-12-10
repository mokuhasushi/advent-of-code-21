import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"

with open(f_in_name) as f_in:
    count = 0
    for line in f_in.readlines():
        sign_patterns, outs = line.split("|")
        sign_patterns = sign_patterns.strip().split(" ")
        outs = outs.strip().split(" ")

        for x in outs:
            if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
                count += 1
    print(count)
