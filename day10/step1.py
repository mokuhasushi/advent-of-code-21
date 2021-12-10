import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"


def score(c):
    if c == ")":
        return 3
    if c == "]":
        return 57
    if c == "}":
        return 1197
    if c == ">":
        return 25137


with open(f_in_name) as f_in:
    sum = 0
    closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
    for line in f_in.readlines():
        line = line.strip()
        control = []
        for c in line:
            if c in {"(", "{", "[", "<"}:
                control.append(closing[c])
            else:
                ex = control.pop()
                if c != ex:
                    sum += score(c)
                    break
    print(sum)
