import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"


def check_lines(board, extracted):
    win_n = [100]
    for line in board:
        picked = 0
        count = 0
        for n in extracted:
            count += 1
            # print(win_n)
            if count > min(win_n):
                break
            if n in line:
                picked += 1
            if picked == 5:
                break
        win_n.append(count)
    return min(win_n)


def check_columns(board, extracted):
    reversed_board = [[l[i] for l in board] for i in range(5)]
    return check_lines(reversed_board, extracted)


def get_winning_time(board, extracted):
    return min(check_lines(board, extracted), check_columns(board, extracted))


def get_board_score(board, extracted):
    flat_list = [item for line in board for item in line if item not in extracted]
    return sum(flat_list)


def read_board_line(f_in):
    line = f_in.readline()

    return list(map(lambda x: int(x), line.split()))


with open(f_in_name) as f_in:
    extracted = list(map(lambda x: int(x), f_in.readline().split(",")))
    losing = 0
    losing_board = None
    while 1:
        try:
            f_in.readline()

            board = [read_board_line(f_in) for _ in range(5)]
            win_time = get_winning_time(board, extracted)
            if win_time > losing:
                losing = win_time
                losing_board = board
        except Exception as e:
            print(e)
            break
    print(get_board_score(losing_board, extracted[:losing]) * extracted[losing - 1])
