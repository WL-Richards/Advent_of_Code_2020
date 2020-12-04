import re
import copy


def part_1(lines):
    # Fields to check for existance
    check_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

    # List of passport data, one entry per passport
    passports = []

    # Number of passports counted
    num_passports = 0

    # Stores tuples of the start and end indexes of the passport data
    passport_start_ends = []

    # Number of valid passports
    valid_passports = 0

    # Parse the input to split able sections
    for i, line in enumerate(lines):

        # Remove newlines and other useless data
        lines[i] = line.strip()

        # If the length of the line is 1 (Which strangely seems to be one) it means there is nothing there
        if len(line) == 1:

            # If it is the first passport being "scanned"
            if num_passports == 0:

                # Start at index 0 for the first value
                passport_start_ends.append((0, i))
                num_passports += 1

            # For all other passports with the exception of the last one uses one plus the previous passports endpoint
            else:
                passport_start_ends.append((passport_start_ends[num_passports - 1][1] + 1, i))
                num_passports += 1

        # If it is the last passport set the end point to the last line in the file
        elif i == len(lines) - 1:
            passport_start_ends.append((passport_start_ends[num_passports - 1][1] + 1, len(lines)))
            num_passports += 1

    # Use the passport indexes to take the data within and convert it to one line no matter its current form
    for i, data in enumerate(passport_start_ends):
        passport = ""
        for data in lines[passport_start_ends[i][0]:passport_start_ends[i][1]]:
            passport += str(data) + " "
        passports.append(passport)

    # Loop through all passports and check if they have the required fields
    for passport in passports:
        valid = True
        for field in check_fields:
            if field not in passport:
                valid = False
                break

        if valid:
            valid_passports += 1

    return valid_passports


def validate_passport(passport):
    """Used for part two to verify that passport data is valid"""

    # Seemingly valid passports that need to be verified
    split_passport_data = passport.split(" ")
    # Remove the last empty index
    del split_passport_data[len(split_passport_data) - 1]

    passport_valid = True

    pass_data = []

    # Split the already split passport data into smaller chunks
    for data in split_passport_data:
        pass_data.append(data.split(":"))

    for key_set in pass_data:
        # Validate Birth Year
        if key_set[0] == "byr":

            # Check if the string is actually a number first
            if not key_set[1].isnumeric():
                passport_valid = False
                break

            # Make sure it is the correct length and it is within the given dates
            if len(key_set[1]) == 4 and 1920 <= int(key_set[1]) <= 2002:
                passport_valid = True
            else:
                passport_valid = False
                break
        # Validate Issue Year
        elif key_set[0] == "iyr":

            # Check if the string is actually a number first
            if not key_set[1].isnumeric():
                passport_valid = False
                break

            # Verify length and date range
            if len(key_set[1]) == 4 and 2010 <= int(key_set[1]) <= 2020:
                passport_valid = True
            else:
                passport_valid = False
                break

        # Validate Expiration Year
        elif key_set[0] == "eyr":

            # Verify length and date range
            if len(key_set[1]) == 4 and 2020 <= int(key_set[1]) <= 2030:
                passport_valid = True
            else:
                passport_valid = False
                break

        # Verify Height
        elif key_set[0] == "hgt":

            # Height without unit
            height = key_set[1][:-2]

            # Check if the string is actually a number first
            if not height.isnumeric():
                passport_valid = False
                break

            # If height is in centimeters
            if "cm" in key_set[1]:
                if 150 <= int(height) <= 193:
                    passport_valid = True
                else:
                    passport_valid = False
                    break

            # If height is inches
            else:
                if 59 <= int(height) <= 76:
                    passport_valid = True
                else:
                    passport_valid = False
                    break

        # Verify Hair Color
        elif key_set[0] == "hcl":

            # Verify the total length is 7
            if len(key_set[1]) == 7:

                # Then check to see if the first character is # signifying a hexcode
                if key_set[1][0] == "#":

                    # Then use regex to determine the alfa-numeric sequence following
                    if re.search("[a-z0-9]{6}", key_set[1][1:]):
                        passport_valid = True
                    else:
                        passport_valid = False
                        break
                else:
                    passport_valid = False
                    break
            else:
                passport_valid = False
                break

        # Verify Eye Color
        elif key_set[0] == "ecl":

            # Just check if the eye color is equal to any of those
            if key_set[1] == "amb" or key_set[1] == "blu" or key_set[1] == "brn" or key_set[1] == "gry" or key_set[
                1] == "grn" or key_set[1] == "hzl" or key_set[1] == "oth":
                passport_valid = True
            else:
                passport_valid = False
                break

        # Verify passport ID
        elif key_set[0] == "pid":

            # Length is 9 and all numbers are numeric (regex is overkill, but I really don't care)
            if len(key_set[1]) == 9:
                if re.search("[0-9]{9}", key_set[1]):
                    passport_valid = True
                else:
                    passport_valid = False
                    break
            else:
                passport_valid = False
                break

    return passport_valid


def part_2(lines):
    check_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    passports = []
    num_passports = 0
    passport_start_ends = []

    # Number of valid passports
    valid_passports = 0

    # Parse the input to split able sections
    for i, line in enumerate(lines):
        lines[i] = line.strip()
        if len(line) == 1:
            if num_passports == 0:
                passport_start_ends.append((0, i))
                num_passports += 1
            else:
                passport_start_ends.append((passport_start_ends[num_passports - 1][1] + 1, i))
                num_passports += 1
        elif i == len(lines) - 1:
            passport_start_ends.append((passport_start_ends[num_passports - 1][1] + 1, len(lines)))
            num_passports += 1

    for i, data in enumerate(passport_start_ends):
        passport = ""
        for data in lines[passport_start_ends[i][0]:passport_start_ends[i][1]]:
            passport += str(data) + " "
        passports.append(passport)

    for passport in passports:
        valid = True
        for field in check_fields:
            if field not in passport:
                valid = False
                break

        if valid:
            if validate_passport(passport):
                valid_passports += 1

    return valid_passports


if __name__ == '__main__':
    # Open and read the lines out of the input file
    input_file = open("input.txt")

    # Separate inputs because I am lazy and just edit the parameter itself, shallow copied into part 2
    part_1_input = input_file.readlines()
    part_2_input = copy.copy(part_1_input)

    print(f"Part 1 Solution: {part_1(part_1_input)} Valid Passports")
    print(f"Part 2 Solution: {part_2(part_2_input)} Valid Passports")
