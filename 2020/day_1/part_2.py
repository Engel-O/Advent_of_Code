with open("input.txt") as f:
    lines = f.readlines()
    
numbers = [int(line) for line in lines]

for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
                exit(0)
