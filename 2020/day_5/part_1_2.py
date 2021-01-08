INPUT_FILE = "input.txt"


def get_position(characters, max_pos):
    left = 0
    right = max_pos

    for c in characters[:-1]:
        if c in ["F", "L"]:
            right -= round((right - left + 1) / 2)
        else:
            left += round((right - left + 1) / 2)

    c = characters[-1]

    if c in ["F", "L"]:
        return min(left, right)
    else:
        return max(left, right)


def part_1():
    with open(INPUT_FILE) as file:
        lines = file.readlines()

    max_value = -1
    for line in lines:
        row_characters = line[:7]
        column_characters = line[7:]

        row = get_position(row_characters, 127)
        col = get_position(column_characters, 7)

        value = row * 8 + col
        max_value = max(value, max_value)

    print(max_value)


def part_2():
    with open(INPUT_FILE) as file:
        lines = file.readlines()

    possible_ids = []
    for row in range(1, 127):
        for col in range(8):
            possible_ids.append(row * 8 + col)

    for line in lines:
        row_characters = line[:7]
        column_characters = line[7:]

        row = get_position(row_characters, 127)
        col = get_position(column_characters, 7)

        possible_ids.remove(row * 8 + col)

    possible_ids.sort()
    for i in range(1, len(possible_ids)):
        if possible_ids[i] - possible_ids[i - 1] > 1 and possible_ids[i + 1] - possible_ids[i] > 1:
            print(possible_ids[i])


if __name__ == "__main__":
    part_1()
    part_2()

