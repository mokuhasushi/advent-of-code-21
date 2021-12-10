import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"


def score(c):
    if c == ")":
        return 1
    if c == "]":
        return 2
    if c == "}":
        return 3
    if c == ">":
        return 4


with open(f_in_name) as f_in:
    scores = []
    closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
    for line in f_in.readlines():
        line = line.strip()
        control = []
        line_score = 0
        incomplete = True
        for c in line:
            if c in {"(", "{", "[", "<"}:
                control.append(closing[c])
            else:
                ex = control.pop()
                if c != ex:
                    incomplete = False
                    break
        if not incomplete:
            continue
        control.reverse()
        for n in control:
            line_score *= 5
            line_score += score(n)
        scores.append(line_score)
    s_scores = sorted(scores)
    print(s_scores[len(s_scores) // 2])
