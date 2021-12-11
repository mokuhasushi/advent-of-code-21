import sys
from typing import Counter

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"


class Dumbo:
    counter: int
    neighbours: list
    flashed = False

    def __init__(self, n, counter):
        self.n = n
        self.counter = counter
        self.neighbours = []

    def add_neighbour(self, n):
        self.neighbours.append(n)

    def increase_count(self):
        self.counter += 1
        if self.counter > 9:
            if not self.flashed:
                self.flash()

    def init_step(self):
        self.flashed = False
        if self.counter > 9:
            self.counter = 0

    def flash(self):
        self.flashed = True
        for n in self.neighbours:
            n.increase_count()

    def __repr__(self):
        return f"octopus n: {self.n}, counter: {self.counter}"


def add_neighbours(i, o, octs):
    if i // 10 != 0:
        o.add_neighbour(octs[i - 10])
        if i % 10 != 0:
            o.add_neighbour(octs[i - 11])
        if i % 10 != 9:
            o.add_neighbour(octs[i - 9])
    if i % 10 != 0:
        o.add_neighbour(octs[i - 1])
    if i % 10 != 9:
        o.add_neighbour(octs[i + 1])
    if i // 10 != 9:
        o.add_neighbour(octs[i + 10])
        if i % 10 != 0:
            o.add_neighbour(octs[i + 9])
        if i % 10 != 9:
            o.add_neighbour(octs[i + 11])


with open(f_in_name) as f_in:
    field = f_in.readlines()
    field = map(lambda s: s.strip(), field)
    field = [int(e) for row in field for e in row]
    octs = []
    for i, n in enumerate(field):
        octs.append(Dumbo(i, n))
    for i, o in enumerate(octs):
        add_neighbours(i, o, octs)
    flash_count = 0
    for _ in range(100):
        list(map(lambda o: o.init_step(), octs))
        list(map(lambda o: o.increase_count(), octs))
        for o in octs:
            if o.flashed:
                flash_count += 1
    print(flash_count)
