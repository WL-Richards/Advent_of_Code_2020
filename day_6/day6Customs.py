def part_1(lines):
    """Solution to part 1 of day 6"""
    group_answers = lines.split("\n\n")
    group_answers = [answer.replace("\n", "") for answer in group_answers]

    yes_sum = 0
    for answer in group_answers:
        # Array of characters with no duplicates
        character_array = []
        for character in answer:
            if character not in character_array:
                character_array.append(character)

        yes_sum += len(character_array)

    return yes_sum


def part_2(lines):
    """Solution to part 2 of day 6"""
    group_answers = lines.split("\n\n")
    single_group_answers = []

    # Split each groups answers into their own list
    for answer in group_answers:
        single_group_answers.append(answer.split("\n"))

    total_sum = 0

    # For every group in the input
    for group in single_group_answers:
        answers_to_look_for = []
        yes_sum = 0

        # Get the answers of the first group member and set those to be the ones to look for
        for answer in group[0]:
            answers_to_look_for.append(answer)

        # Loop through all answers that were in the first one
        for possible_answer in answers_to_look_for:

            # Set the current value of whether or not this answer exists in all to false to start
            all_yes = False

            # Loop over each member in the group
            for member in group:

                # For each member check if the answer is present there, if so set all_yes to true and continue
                # If not set it to false and break
                if possible_answer in member:
                    all_yes = True
                else:
                    all_yes = False
                    break

            # At the end after each member has been looped over if all_yes is still true it means that
            # the answer was present in all members so add one to that group's yes_sum
            if all_yes:
                yes_sum+=1

        total_sum += yes_sum

    # Return the total_sum of all groups
    return total_sum


if __name__ == '__main__':
    input_file = open("input.txt")

    # Clear newlines on all lines, because fuck newlines
    lines = input_file.read()

    print(f"Total Number Of Yes's: {part_1(lines)}")
    print(f"Number Of Questions where everyone answered yes: {part_2(lines)}")
