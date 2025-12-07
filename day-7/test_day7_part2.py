from day7_part2 import create_row_dictionary_splitter_beam_positions

initial_input = [
    [".", ".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "^", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "^", ".", "^", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "^", ".", "^", ".", "^", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "^", ".", "^", ".", ".", ".", "^", ".", ".", ".", "."],
    [".", ".", ".", "^", ".", "^", ".", ".", ".", "^", ".", "^", ".", ".", "."],
    [".", ".", "^", ".", ".", ".", "^", ".", ".", ".", ".", ".", "^", ".", "."],
    [".", "^", ".", "^", ".", "^", ".", "^", ".", "^", ".", ".", ".", "^", "."],
]


def test_create_dictionary_for_first_row():
    overall_dictionary = {}
    input = [
        [".", ".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "^", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "^", ".", "^", ".", ".", ".", ".", ".", "."],
    ]
    row_dictionary = create_row_dictionary_splitter_beam_positions(input[1])
    overall_dictionary[1] = row_dictionary
    result_dictionary = {1: {"splitter7": {"splitter_position": 7, "beam_positions": {6, 8}}}}
    assert overall_dictionary == result_dictionary


data = {
    1: {7: {'beam_positions': {8, 6}}}, 
    2: {6: {'beam_positions': {5, 7}}, 8: {'beam_positions': {9, 7}}}, 
    3: {5: {'beam_positions': {4, 6}}, 7: {'beam_positions': {8, 6}}, 9: {'beam_positions': {8, 10}}}, 
    4: {4: {'beam_positions': {3, 5}}, 6: {'beam_positions': {5, 7}}, 10: {'beam_positions': {9, 11}}}, 
    5: {3: {'beam_positions': {2, 4}}, 5: {'beam_positions': {4, 6}}, 9: {'beam_positions': {8, 10}}, 11: {'beam_positions': {10, 12}}}, 
    6: {2: {'beam_positions': {1, 3}}, 6: {'beam_positions': {5, 7}}, 12: {'beam_positions': {11, 13}}}, 
    7: {1: {'beam_positions': {0, 2}}, 3: {'beam_positions': {2, 4}}, 5: {'beam_positions': {4, 6}}, 7: {'beam_positions': {8, 6}}, 9: {'beam_positions': {8, 10}}, 13: {'beam_positions': {12, 14}}}}




data = {
    1: {7: {'beam_positions': {8, 6}}}, 
    2: {6: {'beam_positions': {5, 7}}, 8: {'beam_positions': {9, 7}}}, 
    3: {5: {'beam_positions': {4, 6}}, 7: {'beam_positions': {6}}, 9: {'beam_positions': {10}}}, 
    4: {4: {'beam_positions': {3, 5}}, 6: {'beam_positions': {5}}, 10: {'beam_positions': {9, 11}}}, 
    5: {3: {'beam_positions': {2}}, 5: {'beam_positions': {6}}, 11: {'beam_positions': {12}}}, 
    6: {2: {'beam_positions': {1, 3}}, 6: {'beam_positions': {5, 7}}, 12: {'beam_positions': {13}}}, 
    7: {1: {'beam_positions': {0, 2}}, 3: {'beam_positions': {2, 4}}, 5: {'beam_positions': {4, 6}}, 7: {'beam_positions': {8, 6}}, 13: {'beam_positions': {12, 14}}}}
def create_viable_paths_dictionary(data):
    for i in range(len(data), 1, -1):
        total_splitters = set()
        for below_row_splitter_position, below_row_beam_positions in data[i].items():
            total_splitters.add(below_row_splitter_position)
        for above_row_splitter_position, above_row_beam_positions in data[i-1].items():
            current_beam_positions_set = above_row_beam_positions["beam_positions"].copy()
            for position in current_beam_positions_set:
                if position not in total_splitters:
                    data[i-1][above_row_splitter_position]["beam_positions"].remove(position)
    for i in range(len(data), 1, -1):
        beam_positions_set = set()
        for above_row_splitter_position, above_row_beam_positions in data[i-1].items():
            beam_positions_set.update(above_row_beam_positions["beam_positions"])
        splitters = set()
        for below_row_splitter_position, below_row_beam_positions in data[i].items():
            if below_row_splitter_position not in beam_positions_set or len(data[i][below_row_splitter_position]["beam_positions"]) == 0:
                splitters.add(below_row_splitter_position)
        for unviable_splitter in splitters:
            del data[i][unviable_splitter]
    

    return data





new_dictionary = create_viable_paths_dictionary(data)
print(new_dictionary)
