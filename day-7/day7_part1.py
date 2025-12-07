from sys import stdin


def get_input():
    overall_list = []
    for line in stdin:
        line_list = list(line.strip())
        if "S" in line_list or "^" in line_list:
            overall_list.append(line_list)
    return overall_list


def get_S_index(input):
    return input[0].index("S")


def beam_split(row, beam_positions, split_number):
    new_beam_positions = beam_positions.copy()
    for position in beam_positions:
        if row[position] == "^":
            new_beam_positions.remove(position)
            new_beam_positions.add(position + 1)
            new_beam_positions.add(position - 1)
            split_number += 1
    print(new_beam_positions)
    return new_beam_positions, split_number


def get_overall_split_number(input):
    index = get_S_index(input)
    beam_positions = {index}
    split_number = 0
    for i in range(1, len(input)):
        beam_positions, split_number = beam_split(
            input[i], beam_positions, split_number
        )
    return split_number


if __name__ == "__main__":
    input = get_input()
    result = get_overall_split_number(input)
    print(result)
