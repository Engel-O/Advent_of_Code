with open("input.txt") as f:
    lines = f.readlines()

valid_passwords = 0
for line in lines:
    line_param = line.strip().split(" ")

    counts = line_param[0].split("-")
    low_count = int(counts[0])
    high_count = int(counts[1])

    char = line_param[1][0]
    password = line_param[2]

    if low_count <= password.count(char) <= high_count:
        valid_passwords += 1

print(valid_passwords)

