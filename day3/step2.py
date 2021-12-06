# with open("sample.txt") as f_in:
with open("input.txt") as f_in:
    ox_gen_list = list(f_in.readlines())
    co2_scrub_list = ox_gen_list.copy()
    input_len = len(ox_gen_list[0]) - 1

    ox_gen = ""
    co2_scrub = ""

    for i in range(input_len):
        ox_bit = [l[i] for l in ox_gen_list]
        ones_o = 0
        zeros_o = 0

        for ob in ox_bit:
            if ob == "0":
                zeros_o += 1
            elif ob == "1":
                ones_o += 1

        if ones_o >= zeros_o:
            ox_gen += "1"
        else:
            ox_gen += "0"

        ox_gen_list = list(filter(lambda x: x.startswith(ox_gen), ox_gen_list))

        if len(ox_gen_list) == 1:
            ox_gen = ox_gen_list[0]
            break

    for i in range(input_len):
        co2_bit = [l[i] for l in co2_scrub_list]
        ones_c = 0
        zeros_c = 0

        for cb in co2_bit:
            if cb == "0":
                zeros_c += 1
            elif cb == "1":
                ones_c += 1
        if ones_c >= zeros_c:
            co2_scrub += "0"
        else:
            co2_scrub += "1"

        co2_scrub_list = list(filter(lambda x: x.startswith(co2_scrub), co2_scrub_list))

        if len(co2_scrub_list) == 1:
            co2_scrub = co2_scrub_list[0]
            break

    ox_n = int(ox_gen, 2)
    co2_n = int(co2_scrub, 2)
    print(ox_n * co2_n)
