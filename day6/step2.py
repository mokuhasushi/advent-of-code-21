import sys

f_in_name = "input.txt"
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        f_in_name = "sample.txt"

with open(f_in_name) as f_in:
    prev = list(map(lambda x: int(x), f_in.readline().split(",")))
    nums = [0] * 9
    for e in prev:
        nums[e] += 1
    for i in range(256):
        sixs = nums[6]
        new_nums = nums[1:7]
        new_nums.append(nums[0])
        new_nums.append(nums[8])
        new_nums.append(nums[0])
        new_nums[6] += nums[7]
        nums = new_nums
        # print(new_nums)
        # new_list += [8 for x in prev if x == 0]
        # prev = new_list
    print(sum(nums))
