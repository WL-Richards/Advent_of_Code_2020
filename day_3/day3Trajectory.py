def duplicate_trees(num_duplicates, lines):
    """Expand the given tree grid out x number of times"""
    # Create duplicated array of trees
    for i, line in enumerate(lines):
        lines[i] = line.strip()
        for _ in range(num_duplicates):
            lines[i] += line.strip()


def right_3_down_1():
    """Check trees with a slope of over 3 down 1"""
    current_x = 0
    tree_count = 0

    for i, line in enumerate(lines):
        if i == 0:
            continue
        current_x += 3
        if line[current_x] == "#":
            tree_count += 1

    return tree_count


def right_1_down_1():
    """Check trees with a slope of over 1 down 1"""
    current_x = 0
    tree_count = 0

    for i, line in enumerate(lines):
        if i == 0:
            continue
        current_x += 1
        if line[current_x] == "#":
            tree_count += 1

    return tree_count


def right_5_down_1():
    """Check trees with a slope of over 5 down 1"""
    current_x = 0
    tree_count = 0

    for i, line in enumerate(lines):
        if i == 0:
            continue
        current_x += 5
        if line[current_x] == "#":
            tree_count += 1

    return tree_count


def right_7_down_1():
    """Check trees with a slope of over 7 down 1"""
    current_x = 0
    tree_count = 0

    for i, line in enumerate(lines):
        if i == 0:
            continue
        current_x += 7
        if line[current_x] == "#":
            tree_count += 1

    return tree_count


def right_1_down_2():
    """Check trees with a slope of over 1 down 2"""
    current_x = 0
    tree_count = 0

    for i, line in enumerate(lines):
        # If its the first line skip it, also skip if it is any number other than an even number
        if i == 0 or i % 2 != 0:
            continue
        current_x += 1
        if line[current_x] == "#":
            tree_count += 1

    return tree_count


def calc_total_trees():
    """Multiply the total tree count together to get the solution to part 2"""
    return right_1_down_1() * right_3_down_1() * right_5_down_1() * right_7_down_1() * right_1_down_2()


if __name__ == '__main__':
    input_file = open("input.txt")
    lines = input_file.readlines()

    # Create an expanded tree array
    duplicate_trees(1000, lines)

    # Print out the solutions
    print("Part 1 Solution: " + str(right_3_down_1()))

    print("Part 2 Solution: " + str(calc_total_trees()))
