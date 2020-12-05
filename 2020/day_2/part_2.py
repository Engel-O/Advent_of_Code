with open("input.txt") as f:
    lines = f.readlines()

valid_passwords = 0
for line in lines:
    line_param = line.strip().split(" ")

    indexes = line_param[0].split("-")
    first_index = int(indexes[0]) - 1
    second_index = int(indexes[1]) - 1

    char = line_param[1][0]
    password = line_param[2]

    count = 0
    if password[first_index] == char:
        count += 1
    if password[second_index] == char:
        count += 1

    if count == 1:
        valid_passwords += 1

print(valid_passwords)

