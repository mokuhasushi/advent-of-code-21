import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"


def calculate_fuel_consumption(positions, x):
    sum = 0
    for e in positions:
        n = abs(e - x)
        sum += (n * (n + 1)) // 2
    return sum


with open(f_in_name) as f_in:
    xs = list(map(int, f_in.readline().split(",")))
    xs_sorted = sorted(xs)
    min_x = xs_sorted[0]
    max_x = xs_sorted[1]

    initials = [0, (min_x + max_x) / 2, max_x - 1]

    candidate = 0
    candidate_fuel = calculate_fuel_consumption(xs, candidate)
    challenger = calculate_fuel_consumption(xs, candidate + 1)
    while challenger < candidate_fuel:
        candidate = candidate + 1
        candidate_fuel = challenger
        challenger = calculate_fuel_consumption(xs, candidate + 1)
    print(candidate, candidate_fuel)
