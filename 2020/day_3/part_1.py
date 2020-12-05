with open("input.txt") as f:
    lines = f.readlines()

trees_encountered = 0
y = 0

line_len = len(lines[0]) - 1

for x in range(len(lines)):
    if lines[x][y] == "#":
        trees_encountered += 1

    y = (y + 3) % line_len


print(trees_encountered)
