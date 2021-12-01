def get_first_window(l):
  return l[0] + l[1] + l[2]
def get_second_window(l):
  return l[1] + l[2] + l[3]

with open("input1.txt") as f_in:
  values = [0,0,0,0]
  values[0] = int(f_in.readline())
  values[1] = int(f_in.readline())
  values[2] = int(f_in.readline())
  values[3] = int(f_in.readline())

  w1 = get_first_window(values) 
  w2 = get_second_window(values)
  count = 0

  if w2 > w1:
    count += 1

  for line in f_in.readlines():
    line_n = int(line)

    values.append(line_n)
    values.pop(0)

    w1 = get_first_window(values) 
    w2 = get_second_window(values)

    if w2 > w1:
      count += 1
  print(count)