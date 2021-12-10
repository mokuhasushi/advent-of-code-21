import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"

# 0 -> 6, no d
# 1 -> 2
# 2 -> 5, no b no f
# 3 -> 5, no b no e
# 4 -> 4
# 5 -> 5, no c no e
# 6 -> 6, no c
# 7 -> 3
# 8 -> 7
# 9 -> 6, no e

# 1 and 7 -> a
# 8 - (a xor b) -> 6
# 6 - d or e (common between 6 and 9, 6 and 0) -> 5 -> e, d -> 0,9
# e in 2, e not in 3
def solve_entry(patterns):
    s_p = sorted(patterns, key=len)
    solutions = {1: set(s_p[0]), 7: set(s_p[1]), 4: set(s_p[2]), 8: set(s_p[9])}
    a = (solutions[7] - solutions[1]).pop()
    six = None
    for candidate in s_p[6:9]:
        six = set(candidate)
        if len(six.intersection(solutions[1])) == 1:
            break
    solutions[6] = six
    three = None
    for candidate in s_p[3:6]:
        three = set(candidate)
        if len(three.intersection(solutions[1])) == 2:
            break
    solutions[3] = three
    nine = None
    for candidate in s_p[6:9]:
        nine = set(candidate)
        if len(nine.intersection(three)) == 5:
            break
    solutions[9] = nine

    for candidate in s_p[3:6]:
        _ca = set(candidate)
        if _ca == three:
            continue
        if len(_ca.intersection(six)) == 5:
            solutions[5] = _ca
        else:
            solutions[2] = _ca

    for z in s_p[6:9]:
        zero = set(z)
        if zero != six and zero != nine:
            break
    solutions[0] = zero
    return solutions


with open(f_in_name) as f_in:
    count = 0
    for line in f_in.readlines():
        sign_patterns, outs = line.split("|")
        sign_patterns = sign_patterns.strip().split(" ")
        outs = outs.strip().split(" ")
        sol = solve_entry(sign_patterns)
        inv_sol = {frozenset(v): k for k, v in sol.items()}
        r_s = ""
        for x in outs:
            r_s += str(inv_sol[frozenset(x)])
        count += int(r_s)
    print(count)
