INPUT_FILE = "input.txt"


def group_generator(file_name):
    with open(file_name) as f:
        file = f.read()

    groups = file.split("\n\n")
    for g in groups:
        yield g.split("\n")


def yes_answers_in_group(group):
    answers = set(group[0])

    for i in range(1, len(group)):
        # answers = answers.intersection(group[i])
        answers = answers.union(group[i])

    return len(answers)


def all_yes_answers_in_group(group):
    answers = set(group[0])

    for i in range(1, len(group)):
        answers = answers.intersection(group[i])

    return len(answers)


def get_answers(count_fun):
    group_gen = group_generator(INPUT_FILE)
    yes_count = 0

    for g in group_gen:
        yes_count += count_fun(g)

    print(yes_count)


if __name__ == "__main__":
    get_answers(yes_answers_in_group)
    get_answers(all_yes_answers_in_group)


