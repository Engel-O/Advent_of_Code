INPUT_FILE = "input.txt"


def load_mapping(with_numbers=False):
    with open(INPUT_FILE) as f:
        lines = f.readlines()

    bag_mapping = {}

    for line in lines:
        if line == "":
            continue

        cur_color, line = line.split("bags contain ")
        line = line.strip()
        cur_color = cur_color.strip()

        bag_mapping[cur_color] = []

        if line == "no other bags.":
            continue

        if "," not in line:
            sub_bags = [line]
        else:
            sub_bags = line.split(",")

        for sub in sub_bags:
            sub = sub.strip()
            num = sub[0]
            color = sub[2: sub.index("bag")]

            if with_numbers:
                bag_mapping[cur_color].append((num, color.strip()))
            else:
                bag_mapping[cur_color].append(color.strip())

    return bag_mapping


def find_containing_bags(mapping, bag_owned, checked=None):
    results = set()

    if checked is None:
        checked = set()

    if bag_owned in checked:
        return results
    else:
        checked.add(bag_owned)

    for k, v in mapping.items():
        if bag_owned in v:
            results.add(k)

    for r in results:
        tmp = find_containing_bags(mapping, r, checked)
        results = results.union(tmp)

    return results


def bags_inside_count(mapping, bag_owned):
    inside_count = 0

    for num, bag in mapping[bag_owned]:
        inside_count += int(num)
        inside_count += int(num) * bags_inside_count(mapping, bag)

    return inside_count


def part_1():
    bag_mapping = load_mapping()
    print(len(find_containing_bags(bag_mapping, "shiny gold")))


def part_2():
    bag_mapping = load_mapping(with_numbers=True)
    print(bags_inside_count(bag_mapping, "shiny gold"))


if __name__ == "__main__":
    part_1()
    part_2()






