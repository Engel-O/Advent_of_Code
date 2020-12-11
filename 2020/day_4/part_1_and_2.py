import re


INPUT_FILE_NAME = "input.txt"
PASSPORT_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
EYE_COLOR = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def passport_generator(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    passport = ""
    for line in lines:
        line = line.strip()

        if not line:
            yield passport
            passport = ""

        passport += line + " "

    if passport:
        yield passport


def is_passport_valid_part1(passport):
    parts = passport.split(" ")

    keys = set()
    for part in parts:
        if not part:
            continue

        key, _ = part.split(":")
        keys.add(key)

    difference = PASSPORT_KEYS.symmetric_difference(keys)

    if len(difference) == 0:
        return True
    elif len(difference) == 1:
        if difference.pop() == "cid":
            return True
    else:
        return False


def check_key_value(key, value):
    if key == "byr":
        return 1920 <= int(value) <= 2002
    elif key == "iyr":
        return 2010 <= int(value) <= 2020
    elif key == "eyr":
        return 2020 <= int(value) <= 2030

    elif key == "hgt":
        if not re.match("[0-9]{2,3}[cm|in]", value):
            return False

        num = int(value[:-2])
        measure = value[-2:]

        if measure == "cm":
            return 150 <= num <= 193
        elif measure == "in":
            return 59 <= num <= 76
        else:
            return False

    elif key == "hcl":
        pattern = "#[0-9||a-f]{6}"
        return re.match(pattern, value)

    elif key == "ecl":
        return value in EYE_COLOR
    elif key == "pid":
        if len(value) != 9:
            return False
        else:
            return value.isnumeric()
    elif key == "cid":
        return True
    else:
        return False


def is_passport_valid_part2(passport):
    parts = passport.split(" ")

    keys = set()
    for part in parts:
        if not part:
            continue

        key, value = part.split(":")
        keys.add(key)

        if not check_key_value(key, value):
            return False

    difference = PASSPORT_KEYS.symmetric_difference(keys)

    if len(difference) == 0:
        return True
    elif len(difference) == 1:
        if difference.pop() == "cid":
            return True
    else:
        return False


def main_loop(validation_function):
    generator = passport_generator(INPUT_FILE_NAME)

    valid_passports = 0
    for passport in generator:
        if validation_function(passport):
            valid_passports += 1

    print(valid_passports)


if __name__ == "__main__":
    # Part 1:
    main_loop(is_passport_valid_part1)

    # Part 2:
    main_loop(is_passport_valid_part2)
