def count_trees_on_slope(lines, right, down):
    line_len = len(lines[0]) - 1
    trees_encountered = 0
    x = y = 0

    while x < len(lines):
        if lines[x][y] == "#":
            trees_encountered += 1

        x += down
        y = (y + right) % line_len

    return trees_encountered


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_mul = 1

    for right, down in slopes:
        trees_mul *= count_trees_on_slope(lines, right, down)

    print(trees_mul)


if __name__ == "__main__":
    main()
