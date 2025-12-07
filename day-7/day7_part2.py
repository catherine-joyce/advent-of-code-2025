from sys import stdin


def create_row_dictionary_splitter_beam_positions(row):
    row_dict = {}
    for i in range(len(row)):
        if row[i] == "^":
            dict_name = i
            new_dict = {"beam_positions": {i - 1, i + 1}}
            row_dict[dict_name] = new_dict
    return row_dict


def create_overall_dictionary(input):
    overall_dictionary = {}
    for i in range(1, len(input)):
        row_dictionary = create_row_dictionary_splitter_beam_positions(input[i])
        overall_dictionary[i] = row_dictionary
    return overall_dictionary


def get_input():
    overall_list = []
    for line in stdin:
        line_list = list(line.strip())
        if "S" in line_list or "^" in line_list:
            overall_list.append(line_list)
    return overall_list


if __name__ == "__main__":
    input = get_input()
    overall_dictionary = create_overall_dictionary(input)
    print(overall_dictionary)
