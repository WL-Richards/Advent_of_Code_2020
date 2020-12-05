import math

def get_seat_ids(lines):
    seat_ids = []

    for line in lines:
        line = line.strip()
        row_range = (0, 127)
        column_range = (0, 7)
        column_num = 0
        row_num = 0
        row_cordinator = line[:-3]
        column_cordinator = line[-3:]
        for i, value in enumerate(row_cordinator):
            # Take the lower half of the current range
            if value == "F":
                row_range = (row_range[0],  math.floor((row_range[1]+row_range[0])/2))
            elif value == "B":
                row_range = (math.ceil((row_range[1]+row_range[0])/2), row_range[1])

        row_num = max(row_range)

        for c, value in enumerate(column_cordinator):
            if value == "L":
                column_range = (column_range[0], math.floor((column_range[1] + column_range[0]) / 2))
            elif value == "R":
                column_range = (math.ceil((column_range[1] + column_range[0]) / 2), column_range[1])

        column_num = max(column_range)

        seat_id = row_num * 8 + column_num
        seat_ids.append(seat_id)
    return seat_ids

def part_1(lines):
    return max(get_seat_ids(lines))

def part_2(lines):
    seats = sorted(get_seat_ids(lines))
    trimed_seats = []

    # Remove duplicates
    for seat in seats:
        if seat not in trimed_seats:
            trimed_seats.append(seat)

    for seat in trimed_seats:
        if (seat + 1) not in seats:
            return (seat + 1)

if __name__ == '__main__':
    input_file = open("input.txt")
    lines = input_file.readlines()

    print(f"Part 1 Solution: Highest Seat # is {part_1(lines)}")
    print(f"Part 2 Solution: My Seat # is {part_2(lines)}")