def part_1_pass_validator(lines):
    """
    Checks the number of occurrences of a letter in the password and if its more than the min and less than the max it is good to go
    """
    valid_passwords = 0
    for line in lines:

        # Split all the given values into variables
        password_char = line.split(" ")[1][:-1].strip()
        min_occurrences = line.split(" ")[0].split("-")[0]
        max_occurrences = line.split(" ")[0].split("-")[1]
        password = line.split(" ")[2].strip()
        occurrences = 0

        # For each occurrence of the password_char in the string add one to the total in that string
        for i, value in enumerate(password):
            if value == password_char:
                occurrences += 1

        # If that total is within (inclusive) the min and max it's valid so add it to the tally
        if int(min_occurrences) <= occurrences <= int(max_occurrences):
            valid_passwords += 1

    # Return the number of valid passwords
    return valid_passwords


def part_2_pass_validator(lines):
    """Checks the positions instead and if only one of those positions is equal to the character its valid"""
    valid_passwords = 0
    for line in lines:

        # Split all the required values into variables
        password_char = line.split(" ")[1][:-1].strip()

        # Convert to index based 0
        pos_1 = int(line.split(" ")[0].split("-")[0])-1
        pos_2 = int(line.split(" ")[0].split("-")[1])-1
        password = line.split(" ")[2].strip()
        password_valid = False
        for i, value in enumerate(password):
            # If the current string index is equal to the first position and the password char is equal to the current
            # set the password as valid
            if i == pos_1:
                if value == password_char:
                    password_valid = True
            # When the second position comes up we need to make sure it is equal to the char and that the other position
            # wasn't the character
            elif i == pos_2:
                if password_valid == True and value == password_char:
                    password_valid = False
                elif password_valid == False and value == password_char:
                    password_valid = True

        # If at the end the password is still valid add one the valid password count
        if password_valid:
            valid_passwords += 1

    # Return the number of valid passwords
    return valid_passwords

if __name__ == '__main__':
    input_file = open("input.txt")
    lines = input_file.readlines()

    print("Part 1 Valid Pass Total: " + str(part_1_pass_validator(lines)))
    print("Part 2 Valid Pass Total: " + str(part_2_pass_validator(lines)))
