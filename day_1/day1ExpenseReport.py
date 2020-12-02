def two_entry_2020_sum(lines):
    """Add up two entries to equal 2020"""
    for line in lines:
        line = line.strip()
        for line_1 in lines:
            line_1 = line_1.strip()
            if int(line) + int(line_1) == 2020:
                print("Two Entry Answer: " + str(int(line) * int(line_1)))
                return None


def three_entry_2020_sum(lines):
    """Add up three entries to equal 2020"""
    for line in lines:
        line = line.strip()
        for line_1 in lines:
            line_1 = line_1.strip()
            for line_2 in lines:
                if int(line) + int(line_1) + int(line_2) == 2020:
                    print("Three Entry Answer: " + str(int(line) * int(line_1) * int(line_2)))
                    return None
2

if __name__ == '__main__':
    input_file = open("input.txt")
    lines = input_file.readlines()
    two_entry_2020_sum(lines)
    three_entry_2020_sum(lines)

